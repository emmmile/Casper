
module.exports = function (grunt) {
    require('load-grunt-tasks')(grunt); // npm install --save-dev load-grunt-tasks

    grunt.initConfig({
        sass: {
            options: {
                sourceMap: true
            },
            dist: {
                files: {
                    'assets/css/additions.css': 'assets/sass/additions.scss'
                }
            }
        }
    });

    grunt.registerTask('default', ['sass']);
};