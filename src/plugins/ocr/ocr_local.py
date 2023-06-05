from nonebot.log import logger

try:
    import easyocr
except ImportError:
    logger.warning("未能成功导入easyocr")

def ocr_local():
    reader = easyocr.Reader(['ch_sim','en'], gpu=True)
    word = reader.readtext("./src/plugins/ocr/ocr.jpg", detail=0)
    result = ""
    for i in word:
        result = result + i + " "
    return result