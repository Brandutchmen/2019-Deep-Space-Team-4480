function timerCheck() {
  var time = NetworkTables.getValue('/SmartDashboard/time');
  var timerOut = document.getElementById("time");
  timerOut.innerHTML = time;
  setTimeout(timerCheck, 100);
  };
timerCheck();
