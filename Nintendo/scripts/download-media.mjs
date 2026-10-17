/** Recria as imagens locais aprovadas no manifesto, sem hotlink ou credenciais. */
import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const media = JSON.parse(await fs.readFile(path.join(root, 'src/data/media.json'), 'utf8'));
const force = process.argv.includes('--force');
const tmp = await fs.mkdtemp(path.join(os.tmpdir(), 'nintendo-media-'));
const python = process.env.CODEX_PRIMARY_RUNTIME_PYTHON || process.env.PYTHON || 'python3';
let done = 0;
try {
  for (const record of media) {
    const url = new URL(record.remoteUrl);
    if (url.protocol !== 'https:' || url.hostname !== 'upload.wikimedia.org') {
      throw new Error(`Origem não autorizada no manifesto: ${record.id}`);
    }
    const name = path.basename(record.src);
    if (record.src !== `/media/${name}` || !name.endsWith('.webp')) {
      throw new Error(`Destino inválido: ${record.id}`);
    }
    const target = path.join(root, 'public/media', name);
    if (!force && await fs.stat(target).then(() => true, () => false)) {
      console.log(`Já presente: ${name}`);
      continue;
    }
    const original = path.join(tmp, name + '.original');
    const download = spawnSync('curl', ['-L', '--fail', '--silent', '--show-error', '--max-time', '60', url.href, '-o', original], { stdio: 'inherit' });
    if (download.status !== 0) throw new Error(`Falha de download: ${name}`);
    await fs.mkdir(path.dirname(target), { recursive: true });
    const resize = spawnSync(python, ['-c',
      "from PIL import Image; import sys; im=Image.open(sys.argv[1]); im.load(); im.thumbnail((1200,1200),Image.Resampling.LANCZOS); im.save(sys.argv[2],'WEBP',quality=86,method=6)",
      original, target
    ], { stdio: 'inherit' });
    if (resize.status !== 0) throw new Error('A conversão requer Python 3 e Pillow. Veja docs/MIDIA.md.');
    console.log(`Salvo: ${name} — ${record.author} — ${record.license}`);
    done++;
  }
  console.log(`${done} imagem(ns) recuperada(s). Os créditos permanecem em src/data/media.json.`);
} finally {
  await fs.rm(tmp, { recursive: true, force: true });
}
