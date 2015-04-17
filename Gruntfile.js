module.exports = function (grunt) {
    grunt.initConfig({
        paths: {
            scss: './scss',
            css: './assets/css'
        },
        buildType: 'Build',
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            admin: {
                options : {
                    // Only enable sourcemaps if you have Sass 3.3 installed.
                    // sourcemap: true
                },
                files: {
                    '<%= paths.css %>/additions.css': '<%= paths.scss %>/additions.scss'
                }
            }
        },

        watch: {
            sass: {
                files: './scss/*.scss',
                tasks: ['sass:admin']
            }
        }
    });


    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['sass:admin']);
};