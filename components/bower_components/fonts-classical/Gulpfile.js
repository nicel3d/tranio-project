var gulp  = require('gulp'),
    minifyCss = require('gulp-minify-css')
    clean = require('gulp-rimraf'),
    rename = require('gulp-rename');

var taskListing = require('gulp-task-listing');


gulp.task('clean', function () {
  return gulp.src('css', {read: false})
    .pipe(clean());
});

gulp.task('minify', function() {
  return gulp.src('src/css/fonts-classical.css')
    .pipe(minifyCss({compatibility: 'ie8'}))
    .pipe(rename({suffix: '.min'}))
    .pipe(gulp.dest('css'));
});

// Help tasks
gulp.task('help', taskListing);
// Default task
gulp.task('default', ['clean','minify']);

