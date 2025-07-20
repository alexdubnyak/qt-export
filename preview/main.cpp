#include <QApplication>
#include <QMainWindow>
#include <QFile>
#include <QTextStream>
#include <QUiLoader>
#include <QWidget>
#include <QDebug>
#include <QMessageBox>
#include <QDir>

/**
 * Qt Components Preview - Figma Export
 * Приложение для предпросмотра компонентов, экспортированных из Figma
 * 
 * Загружает form.ui и применяет style.qss для отображения 
 * всех вариантов кнопок из дизайн-системы Figma
 */

class FigmaPreviewApp : public QObject
{
    Q_OBJECT

public:
    FigmaPreviewApp(QObject *parent = nullptr) : QObject(parent) {}

    bool loadUI(const QString &uiFile, const QString &styleFile) 
    {
        // Загрузка UI файла
        QUiLoader loader;
        QFile file(uiFile);
        
        if (!file.open(QIODevice::ReadOnly)) {
            qCritical() << "❌ Не удается открыть" << uiFile;
            showError(QString("Не удается открыть UI файл: %1").arg(uiFile));
            return false;
        }

        m_widget = loader.load(&file);
        file.close();

        if (!m_widget) {
            qCritical() << "❌ Не удается загрузить UI";
            showError("Не удается загрузить UI файл");
            return false;
        }

        qDebug() << "✅ UI файл загружен успешно";

        // Применение стилей
        loadStyleSheet(styleFile);

        // Настройка окна
        m_widget->setWindowTitle("🎨 Figma Qt Export - Components Preview");
        m_widget->resize(1200, 800);
        
        return true;
    }

    void show() 
    {
        if (m_widget) {
            m_widget->show();
            qDebug() << "✅ Окно предпросмотра отображено";
        }
    }

private:
    QWidget *m_widget = nullptr;

    void loadStyleSheet(const QString &styleFile) 
    {
        QFile file(styleFile);
        if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
            qWarning() << "⚠️ Не удается открыть файл стилей:" << styleFile;
            return;
        }

        QTextStream stream(&file);
        QString styleSheet = stream.readAll();
        
        if (m_widget) {
            m_widget->setStyleSheet(styleSheet);
            qDebug() << "✅ Стили применены успешно";
        }
        
        file.close();
    }

    void showError(const QString &message) 
    {
        QMessageBox::critical(nullptr, "Ошибка загрузки", message);
    }
};

bool checkEnvironment() 
{
    qDebug() << "🔍 Проверка окружения...";
    
    QStringList requiredFiles = {"form.ui", "style.qss"};
    QStringList missingFiles;
    
    for (const QString &fileName : requiredFiles) {
        if (!QFile::exists(fileName)) {
            missingFiles << fileName;
        }
    }
    
    if (!missingFiles.isEmpty()) {
        qWarning() << "⚠️ Отсутствуют файлы:" << missingFiles.join(", ");
        return false;
    }
    
    qDebug() << "✅ Все необходимые файлы найдены";
    
    // Проверка директории с иконками (опционально)
    QDir iconsDir("icons");
    if (iconsDir.exists()) {
        QStringList svgFiles = iconsDir.entryList(QStringList() << "*.svg", QDir::Files);
        qDebug() << "🎨 Найдено" << svgFiles.count() << "SVG иконок";
    } else {
        qDebug() << "ℹ️ Директория icons не найдена (это нормально)";
    }
    
    return true;
}

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    
    // Настройка приложения
    app.setApplicationName("Figma Qt Export Preview");
    app.setApplicationVersion("1.0.0");
    app.setOrganizationName("Figma Qt Export");
    
    qDebug() << "🚀 Запуск Qt Components Preview";
    qDebug() << "📱 Система экспорта Figma → Qt";
    qDebug() << QString(50, '-');
    
    // Проверка окружения
    if (!checkEnvironment()) {
        qCritical() << "❌ Проверка окружения не пройдена";
        QMessageBox::critical(
            nullptr, 
            "Ошибка инициализации",
            "Отсутствуют необходимые файлы (form.ui, style.qss).\\n"
            "Убедитесь, что все файлы находятся в той же директории."
        );
        return -1;
    }
    
    // Создание и запуск приложения предпросмотра
    FigmaPreviewApp preview;
    
    if (!preview.loadUI("form.ui", "style.qss")) {
        qCritical() << "❌ Не удается инициализировать предпросмотр";
        return -1;
    }
    
    preview.show();
    
    qDebug() << "ℹ️ Нажмите на любую кнопку для взаимодействия";
    qDebug() << QString(50, '-');
    
    return app.exec();
}

#include "main.moc"
