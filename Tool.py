# Developer : Lucas Liu
# Date: 6/5/2022 Time: 6:56

class QSSTool:
    @staticmethod
    def setQssTool(file_path, obj):
        with open(file_path, 'r') as f:
            qss_style = f.read()
            obj.setStyleSheet(qss_style)
