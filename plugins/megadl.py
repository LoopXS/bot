"""
✘ Commands Available -

•`{i}megadl <link>`
  It Downloads and Upload Files from mega.nz links.
"""
import time
from datetime import datetime

from . import (
    HNDLR,
    LOGS,
    bash,
    eor,
    get_all_files,
    get_string,
    humanbytes,
    os,
    time_formatter,
    ultroid_cmd,
    uploader,
)


@ultroid_cmd(pattern="megadl ?(.*)")
async def _(e):
    link = e.pattern_match.group(1)
    if os.path.isdir("mega"):
        await bash("rm -rf mega")
    os.mkdir("mega")
    xx = await eor(e, f"{get_string('com_1')}\nTo Check Progress : `{HNDLR}ls mega`")
    s = datetime.now()
    x, y = await bash(f"megadl {link} --path mega")
    ok = get_all_files("mega")
    tt = time.time()
    c = 0
    for kk in ok:
        try:
            res = await uploader(kk, kk, tt, xx, get_string("com_6"))
            await e.client.send_file(
                e.chat_id,
                res,
                caption="`" + kk.split("/")[-1] + "`",
                force_document=True,
                thumb="resources/extras/cipherx.jpg",
            )
            c += 1
        except Exception as er:
            LOGS.info(er)
    ee = datetime.now()
    t = time_formatter(((ee - s).seconds) * 1000)
    size = 0
    for path, dirs, files in os.walk("mega"):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    await xx.delete()
    await e.client.send_message(
        e.chat_id,
        f"Downloaded And Uploaded Total - `{c}` files of `{humanbytes(size)}` in `{t}`",
    )
    await bash("rm -rf mega")
