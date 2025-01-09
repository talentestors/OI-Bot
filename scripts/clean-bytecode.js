// filepath: nonebot-plugin-oi-helper/scripts/clean-pycache.js
const fs = require('fs');
const path = require('path');

function deletePycache(dir) {
    fs.readdir(dir, (err, files) => {
        if (err) {
            console.error(`Error reading directory ${dir}: ${err}`);
            return;
        }

        files.forEach(file => {
            const filePath = path.join(dir, file);
            fs.stat(filePath, (err, stats) => {
                if (err) {
                    console.error(`Error stating file ${filePath}: ${err}`);
                    return;
                }

                if (stats.isDirectory()) {
                    if (file === '__pycache__') {
                        fs.rmdir(filePath, { recursive: true }, (err) => {
                            if (err) {
                                console.error(`Error removing directory ${filePath}: ${err}`);
                            } else {
                                console.log(`Removed directory ${filePath}`);
                            }
                        });
                    } else if (file !== '.venv') {
                        deletePycache(filePath);
                    }
                }
            });
        });
    });
}

deletePycache(process.cwd());
