function controllerCheck() {
  var x = NetworkTables.getValue('/SmartDashboard/ctrlY');
  var controllerOut = document.getElementById("controllerY");
  controllerOut.innerHTML = x;
  setTimeout(controllerCheck, 100);
  };

controllerCheck();
