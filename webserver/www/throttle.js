var ProgressBar = require('progressbar.js')

function init() {

    var bar = new ProgressBar.Circle(throttle, {
    color: '#14876C',
    // This has to be the same size as the maximum width to
    // prevent clipping
    strokeWidth: 5,
    trailWidth: 5,
    trailColor: '#D3D3D3',
    easing: 'easeInOut',
    duration: 150,
    text: {
      autoStyleContainer: false
    },
    from: { color: '#FF652F', width: 5 },
    to: { color: '#14876C', width: 5 },
    // Set default step function for all animate calls
    step: function(state, circle) {
      circle.path.setAttribute('stroke', state.color);
      circle.path.setAttribute('stroke-width', state.width);

      var value = Math.round(circle.value() * 100);
      if (value === 0) {
        circle.setText('Left');
      } else {
        circle.setText(value+"%");
      }

    }
  });
  bar.text.style.fontFamily = '"Raleway", Helvetica, sans-serif';
  bar.text.style.fontSize = '2rem';

  var x = NetworkTables.getValue('/SmartDashboard/ctrlY', '0.0');
  bar.animate(x);  // Value from 0.0 to 1.0
  loop();

  function loop() {

  //  var x = NetworkTables.getValue('/SmartDashboard/ctrlY');
    var x = NetworkTables.getValue('/SmartDashboard/ctrlY', '0.0');
    bar.animate(x);  // Value from 0.0 to 1.0

    setTimeout(loop, 100);
    };
}
init();
