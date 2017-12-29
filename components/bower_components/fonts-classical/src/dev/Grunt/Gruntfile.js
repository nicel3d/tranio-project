module.exports = function (grunt) {

  require('load-grunt-tasks')(grunt);

  grunt.initConfig ({
    pkg : grunt.file.readJSON('package.json'),

    clean: {
      css: ['css/fonts-classical.min.css']
    },

    cssmin :{
      app : {
        files : {
          'css/fonts-classical.min.css': 'src/css/fonts-classical.css'
        }
      }
    },

    // List available Grunt tasks & targets.
  availabletasks: {
    tasks: {
         options: {
            filter: 'exclude',
            tasks: ['availabletasks', 'default'],
            descriptions: {
               'build': 'Compile.'
            },
             showTasks: ['user']
        }
    }
  }


  });


// -------------------------------------------------------------------------------------

  // Load available-tasks
 grunt.loadNpmTasks('grunt-available-tasks');
  // Default task
 grunt.registerTask('help', [ 'availabletasks']);

 grunt.registerTask('default', 'Starts build', function (target) {
    var tasks = {
      prep_build: [
        'clean'
      ],
      post_build:[
        'cssmin'
      ],
       default: [
        'default:prep_build'
        ,'default:post_build'
      ]
    };

    grunt.task.run(tasks[target] || tasks['default']);
 });

};
