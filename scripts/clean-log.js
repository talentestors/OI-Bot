const fs = require('fs');
const path = require('path');

function cleanLogs(dir) {
    fs.readdir(dir, (err, files) => {
        if (err) {
            console.error(`Error reading directory: ${dir}`, err);
            return;
        }

        files.forEach((file) => {
            const filePath = path.join(dir, file);

            fs.stat(filePath, (err, stats) => {
                if (err) {
                    console.error(`Error getting stats for file: ${filePath}`, err);
                    return;
                }

                if (stats.isFile() && file.endsWith('.log')) {
                    // Delete .log files
                    fs.unlink(filePath, (err) => {
                        if (err) {
                            console.error(`Error deleting file: ${filePath}`, err);
                        } else {
                            console.log(`Deleted file: ${filePath}`);
                        }
                    });
                } else if (stats.isDirectory() && file.endsWith('log')) {
                    // Delete directories ending with 'log'
                    fs.rm(filePath, { recursive: true, force: true }, (err) => {
                        if (err) {
                            console.error(`Error deleting directory: ${filePath}`, err);
                        } else {
                            console.log(`Deleted directory: ${filePath}`);
                        }
                    });
                }
            });
        });
    });
}

// Start cleaning logs
cleanLogs(process.cwd());
