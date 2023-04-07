import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Python Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Python Demo'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  void _runPythonProgram() async {
    // Replace the URL with your server-side API endpoint that runs the Python program
    String url = 'http://127.0.0.1:5000/runastar';
    http.Response response = await http.post(Uri.parse(url));
    if (response.statusCode == 200) {
      print('Python program executed successfully');
    } else {
      print('Failed to execute Python program');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: _runPythonProgram,
          child: Text('Run Python Program'),
        ),
      ),
    );
  }
}