#include <QApplication>
#include <QWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QUiLoader>
#include <QFile>
#include <QTextStream>
#include <QPixmap>
#include <QSvgRenderer>
#include <QPainter>

class QAbstractButtonExample : public QWidget
{
    Q_OBJECT

public:
    QAbstractButtonExample(QWidget *parent = nullptr) : QWidget(parent)
    {
        setupUI();
        loadStyles();
    }

private:
    void setupUI()
    {
        setWindowTitle("QAbstractButton - Exported from Figma");
        setFixedSize(300, 200);
        
        QVBoxLayout *mainLayout = new QVBoxLayout(this);
        
        // Create button using exported UI structure
        QWidget *buttonWidget = createButtonFromExport();
        mainLayout->addWidget(buttonWidget);
        
        // Add some spacing
        mainLayout->addSpacing(20);
        
        // Create variations
        createButtonVariations(mainLayout);
        
        mainLayout->addStretch();
    }
    
    QWidget* createButtonFromExport()
    {
        // Create the main button widget matching Figma export
        QWidget *buttonWidget = new QWidget;
        buttonWidget->setObjectName("QAbstractButtonWidget");
        buttonWidget->setFixedSize(60, 24);
        
        // Create layout matching Figma structure
        QHBoxLayout *layout = new QHBoxLayout(buttonWidget);
        layout->setContentsMargins(8, 4, 8, 4);
        layout->setSpacing(4);
        
        // Create icon label
        QLabel *iconLabel = new QLabel;
        iconLabel->setObjectName("iconLabel");
        iconLabel->setFixedSize(16, 16);
        
        // Load and set the SVG icon
        QSvgRenderer renderer(QString(":/icons/src/resources/qabstract_button_icon.svg"));
        QPixmap pixmap(16, 16);
        pixmap.fill(Qt::transparent);
        QPainter painter(&pixmap);
        renderer.render(&painter);
        iconLabel->setPixmap(pixmap);
        
        // Create text label
        QLabel *textLabel = new QLabel("Label");
        textLabel->setObjectName("textLabel");
        
        layout->addWidget(iconLabel);
        layout->addWidget(textLabel);
        
        return buttonWidget;
    }
    
    void createButtonVariations(QVBoxLayout *mainLayout)
    {
        // Different sizes
        mainLayout->addWidget(new QLabel("Size Variations:"));
        
        QHBoxLayout *sizesLayout = new QHBoxLayout;
        
        // Small button
        QWidget *smallBtn = createButtonFromExport();
        smallBtn->setProperty("size", "sm");
        sizesLayout->addWidget(smallBtn);
        
        // Medium button  
        QWidget *mediumBtn = createButtonFromExport();
        mediumBtn->setProperty("size", "md");
        mediumBtn->setFixedSize(80, 32);
        sizesLayout->addWidget(mediumBtn);
        
        // Large button
        QWidget *largeBtn = createButtonFromExport();
        largeBtn->setProperty("size", "lg");
        largeBtn->setFixedSize(100, 40);
        sizesLayout->addWidget(largeBtn);
        
        mainLayout->addLayout(sizesLayout);
        
        // Different types
        mainLayout->addWidget(new QLabel("Type Variations:"));
        
        QHBoxLayout *typesLayout = new QHBoxLayout;
        
        // QPushButton type
        QWidget *pushBtn = createButtonFromExport();
        pushBtn->setProperty("type", "QPushButton");
        typesLayout->addWidget(pushBtn);
        
        // QToolButton icon type
        QWidget *toolBtn = createButtonFromExport();
        toolBtn->setProperty("type", "QToolButton_icon");
        typesLayout->addWidget(toolBtn);
        
        mainLayout->addLayout(typesLayout);
    }
    
    void loadStyles()
    {
        // Load the exported QSS styles
        QFile styleFile(":/styles/src/styles/qabstract_button.qss");
        if (styleFile.open(QFile::ReadOnly | QFile::Text)) {
            QTextStream stream(&styleFile);
            QString style = stream.readAll();
            setStyleSheet(style);
        }
    }
};

// Alternative method using QUiLoader for .ui files
class QAbstractButtonFromUI : public QWidget
{
    Q_OBJECT
    
public:
    QAbstractButtonFromUI(QWidget *parent = nullptr) : QWidget(parent)
    {
        loadFromUI();
    }
    
private:
    void loadFromUI()
    {
        QUiLoader loader;
        QFile file(":/widgets/src/widgets/qabstract_button.ui");
        
        if (file.open(QFile::ReadOnly)) {
            QWidget *loadedWidget = loader.load(&file, this);
            file.close();
            
            if (loadedWidget) {
                QVBoxLayout *layout = new QVBoxLayout(this);
                layout->addWidget(loadedWidget);
                
                // Load styles
                QFile styleFile(":/styles/src/styles/qabstract_button.qss");
                if (styleFile.open(QFile::ReadOnly | QFile::Text)) {
                    QTextStream stream(&styleFile);
                    QString style = stream.readAll();
                    loadedWidget->setStyleSheet(style);
                }
            }
        }
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    
    // Method 1: Manual creation matching Figma export
    QAbstractButtonExample window1;
    window1.show();
    window1.move(100, 100);
    
    // Method 2: Using QUiLoader with .ui file
    QAbstractButtonFromUI window2;
    window2.show();
    window2.move(450, 100);
    
    return app.exec();
}

#include "main.moc"
