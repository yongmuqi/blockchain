

class textFile:
    # 写入TXT功能
    @staticmethod
    def write_txt_data(data: str or int):
        with open('C:\\Users\\chencheng\\PycharmProjects\\adsTask\\taskCode\\config\\log.txt', "a", encoding="utf-8") as f:
            f.write(data + '\n')
            f.close()
