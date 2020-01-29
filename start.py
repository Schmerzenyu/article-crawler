import sys

from PyQt5.QtWidgets import QApplication

from Crawler import ArticleCrawler

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = ArticleCrawler()

    sys.exit(app.exec_())

