#include <QApplication>
#include <QMainWindow>
#include <QFile>
#include <QTextStream>
#include <QUiLoader>
#include <QWidget>
#include <QDebug>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QUiLoader loader;
    QFile file("form.ui");
    if (!file.open(QIODevice::ReadOnly)) {
        qDebug() << "Cannot open form.ui";
        return -1;
    }

    QWidget *widget = loader.load(&file);
    file.close();

    if (!widget) {
        qDebug() << "Cannot load UI";
        return -1;
    }

    QFile styleFile("style.qss");
    if (styleFile.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QTextStream stream(&styleFile);
        QString styleSheet = stream.readAll();
        widget->setStyleSheet(styleSheet);
        styleFile.close();
        qDebug() << "Styles applied successfully";
    } else {
        qDebug() << "Cannot load style.qss";
    }

    widget->setWindowTitle("Qt Components Preview - QAbstractButton Export from Figma");
    widget->show();
    
    return app.exec();
}
