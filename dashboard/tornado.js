function tornado() {

    let {PythonShell} = require('python-shell')
    PythonShell.run('tornado_server.py', null, function (err) {
    if (err) throw err;
      console.log('finished');
    });
}

tornado();
