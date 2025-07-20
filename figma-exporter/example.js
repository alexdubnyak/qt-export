// Example: Using Figma to Qt Exporter with real Figma data
import { FigmaToQtExporter } from './figma-to-qt.js';

// Example Figma design variables extracted from your component set
const figmaDesignVariables = {
    "Theme/GeneralUI/Icons/active": "#bbbbbb",
    "Theme/GeneralUI/Icons/surface": "#efefef",
    "Theme/QLabel/label:active": "#3f3f3f",
    "Grid/Font Size/small": "12",
    "Grid/Spacing/spacing-xxs": "4",
    "Grid/Spacing/spacing-none": "0",
    "Grid/Radius/radius-sm": "4",
    "xxsmall": "4",
    "small": "8", 
    "Grid/Widgets Size/Small": "24",
    "Theme/QAbstractButton/surface:active": "#e2e2e2",
    "Theme/QAbstractButton/border:active": "#bbbbbb",
    "Theme/QAbstractButton/border:hover": "#85cfeb",
    "Theme/QAbstractButton/surface:hover": "#dff4fa",
    "Theme/QAbstractButton/surface:pressed": "#b1e2f2",
    "Theme/QAbstractButton/border:pressed": "#4faade",
    "Theme/QLabel/label:disabled": "#bbbbbb",
    "Theme/QAbstractButton/surface:disabled": "#e2e2e2",
    "Theme/QAbstractButton/border:disabled": "#bbbbbb",
    "Grid/Font Size/medium": "14",
    "Grid/Widgets Size/Medium": "32",
    "Grid/Font Size/large": "16",
    "Grid/Widgets Size/Large": "40",
    "Theme/GeneralUI/label:active": "#222222",
    "none": "0",
    "Theme/QAbstractButton/divider": "#bbbbbb",
    "Grid/Radius/radius-none": "0",
    "Grid/Radius/radius-xxs": "4",
    "medium": "12",
    "Theme/GeneralUI/label:disabled": "#bbbbbb"
};

// Sample Figma component data (normally this would come from Figma API)
const sampleFigmaData = `
<div data-name="Size=sm, State=active, Type=QPushButton" className="bg-[#e2e2e2]">
<div data-name="Size=sm, State=hover, Type=QPushButton" className="bg-[#dff4fa]">
<div data-name="Size=sm, State=pressed, Type=QPushButton" className="bg-[#b1e2f2]">
<div data-name="Size=sm, State=disabled, Type=QPushButton" className="bg-[#e2e2e2]">
<div data-name="Size=md, State=active, Type=QPushButton" className="bg-[#e2e2e2]">
<div data-name="Size=md, State=hover, Type=QPushButton" className="bg-[#dff4fa]">
<div data-name="Size=md, State=pressed, Type=QPushButton" className="bg-[#b1e2f2]">
<div data-name="Size=md, State=disabled, Type=QPushButton" className="bg-[#e2e2e2]">
<div data-name="Size=lg, State=active, Type=QPushButton" className="bg-[#e2e2e2]">
<div data-name="Size=lg, State=hover, Type=QPushButton" className="bg-[#dff4fa]">
<div data-name="Size=lg, State=pressed, Type=QPushButton" className="bg-[#b1e2f2]">
<div data-name="Size=lg, State=disabled, Type=QPushButton" className="bg-[#e2e2e2]">
<div data-name="Size=sm, State=active, Type=QToolButton_icon" className="bg-[#e2e2e2]">
<div data-name="Size=sm, State=hover, Type=QToolButton_icon" className="bg-[#dff4fa]">
<div data-name="Size=sm, State=pressed, Type=QToolButton_icon" className="bg-[#b1e2f2]">
<div data-name="Size=sm, State=disabled, Type=QToolButton_icon" className="bg-[#e2e2e2]">
<div data-name="Size=md, State=active, Type=QToolButton_icon" className="bg-[#e2e2e2]">
<div data-name="Size=md, State=hover, Type=QToolButton_icon" className="bg-[#dff4fa]">
<div data-name="Size=md, State=pressed, Type=QToolButton_icon" className="bg-[#b1e2f2]">
<div data-name="Size=md, State=disabled, Type=QToolButton_icon" className="bg-[#e2e2e2]">
<div data-name="Size=lg, State=active, Type=QToolButton_icon" className="bg-[#e2e2e2]">
<div data-name="Size=lg, State=hover, Type=QToolButton_icon" className="bg-[#dff4fa]">
<div data-name="Size=lg, State=pressed, Type=QToolButton_icon" className="bg-[#b1e2f2]">
<div data-name="Size=lg, State=disabled, Type=QToolButton_icon" className="bg-[#e2e2e2]">
<div data-name="Size=sm, State=active, Type=QToolButton_arrow" className="bg-[#e2e2e2]">
<div data-name="Size=sm, State=hover, Type=QToolButton_arrow" className="bg-[#dff4fa]">
<div data-name="Size=sm, State=pressed, Type=QToolButton_arrow" className="bg-[#b1e2f2]">
<div data-name="Size=sm, State=disabled, Type=QToolButton_arrow" className="bg-[#e2e2e2]">
<div data-name="Size=md, State=active, Type=QToolButton_arrow" className="bg-[#e2e2e2]">
<div data-name="Size=md, State=hover, Type=QToolButton_arrow" className="bg-[#dff4fa]">
<div data-name="Size=md, State=pressed, Type=QToolButton_arrow" className="bg-[#b1e2f2]">
<div data-name="Size=md, State=disabled, Type=QToolButton_arrow" className="bg-[#e2e2e2]">
<div data-name="Size=lg, State=active, Type=QToolButton_arrow" className="bg-[#e2e2e2]">
<div data-name="Size=lg, State=hover, Type=QToolButton_arrow" className="bg-[#dff4fa]">
<div data-name="Size=lg, State=pressed, Type=QToolButton_arrow" className="bg-[#b1e2f2]">
<div data-name="Size=lg, State=disabled, Type=QToolButton_arrow" className="bg-[#e2e2e2]">
`;

// Usage example
function exportFromFigma() {
    const exporter = new FigmaToQtExporter();
    
    // Export complete package
    const exportResult = exporter.exportComplete(
        sampleFigmaData, 
        figmaDesignVariables, 
        "ButtonComponents"
    );
    
    console.log("=== Generated QSS ===");
    console.log(exportResult.qss);
    
    console.log("\n=== Generated UI ===");
    console.log(exportResult.ui);
    
    console.log("\n=== Export Info ===");
    console.log(`Generated at: ${exportResult.timestamp}`);
    
    return exportResult;
}

// Integration with Figma Web API (example)
async function exportFromFigmaAPI(fileKey, nodeId) {
    try {
        // This would require Figma API token
        const response = await fetch(`https://api.figma.com/v1/files/${fileKey}/nodes?ids=${nodeId}`, {
            headers: {
                'X-Figma-Token': 'YOUR_FIGMA_TOKEN'
            }
        });
        
        const figmaData = await response.json();
        
        // Extract component data and variables
        const exporter = new FigmaToQtExporter();
        const result = exporter.exportComplete(figmaData, figmaDesignVariables);
        
        return result;
    } catch (error) {
        console.error('Error exporting from Figma API:', error);
        throw error;
    }
}

// Save files to disk (Node.js environment)
function saveExportToDisk(exportResult, outputDir = './output') {
    const fs = require('fs');
    const path = require('path');
    
    // Create output directory
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }
    
    // Save QSS file
    fs.writeFileSync(
        path.join(outputDir, 'components.qss'), 
        exportResult.qss
    );
    
    // Save UI file
    fs.writeFileSync(
        path.join(outputDir, 'components.ui'), 
        exportResult.ui
    );
    
    // Save metadata
    fs.writeFileSync(
        path.join(outputDir, 'export-info.json'), 
        JSON.stringify({
            timestamp: exportResult.timestamp,
            generatedFiles: ['components.qss', 'components.ui']
        }, null, 2)
    );
    
    console.log(`Files saved to ${outputDir}`);
}

// Export functions for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        exportFromFigma,
        exportFromFigmaAPI,
        saveExportToDisk,
        figmaDesignVariables,
        sampleFigmaData
    };
}

// Example usage
if (typeof window === 'undefined') {
    // Node.js environment
    const result = exportFromFigma();
    console.log('Export completed successfully!');
}
