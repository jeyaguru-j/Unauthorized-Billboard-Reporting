import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;

class UploadScreen extends StatefulWidget {
  @override
  _UploadScreenState createState() => _UploadScreenState();
}

class _UploadScreenState extends State<UploadScreen> {
  File? _image;

  Future pickImage() async {
    final pickedFile = await ImagePicker().pickImage(source: ImageSource.camera);
    setState(() {
      _image = File(pickedFile!.path);
    });
  }

  Future uploadImage() async {
    if (_image == null) return;
    var request = http.MultipartRequest(
      'POST', Uri.parse('http://127.0.0.1:5000/report')
    );
    request.files.add(await http.MultipartFile.fromPath('image', _image!.path));
    request.fields['user_name'] = 'John Doe';
    request.fields['latitude'] = '12.9716';
    request.fields['longitude'] = '77.5946';

    var res = await request.send();
    print(await res.stream.bytesToString());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Report Billboard')),
      body: Column(
        children: [
          _image != null ? Image.file(_image!) : Container(),
          ElevatedButton(onPressed: pickImage, child: Text('Take Photo')),
          ElevatedButton(onPressed: uploadImage, child: Text('Submit Report'))
        ],
      ),
    );
  }
}
