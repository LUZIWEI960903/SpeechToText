var recorder;
var audio = document.querySelector('audio');
// var WAV_audio//音频文件sadasdasdf
// var base64_WAV_audio//64位音频

// 转URL
function blobToDataURL(blob, callback) {
    var a = new FileReader();
    a.onload = function (e) { callback(e.target.result); }
    a.readAsDataURL(blob);
}


// function getData(audioFile) {
//     var reader = new FileReader();
//     reader.onload = function (event) {
//         var data = event.target.result.split(',');
//         decodedImageData = btoa(data[1]);// the actual conversion of data from binary to base64 format
//         // callback(decodedImageData);
//     };
//     reader.readAsDataURL(audioFile);
// }

function changeStatus(id_a, id_b) {
    var a = document.getElementById(id_a);
    var b = document.getElementById(id_b);
    temp = a.style.display;
    a.style.display = 'none';
    b.style.display = temp;
}

function startRecording(a, b) {
    HZRecorder.get(function (rec) {
        recorder = rec;
        recorder.start();
    });
    changeStatus(a, b)
}
function stopRecording(a, b) {
    recorder.stop();
    changeStatus(a, b);
    // playRecording();
    WAV_audio = recorder.getBlob();
    console.info(Object.prototype.toString.call(WAV_audio));
    // console.info(WAV_audio);
    // base64_WAV_audio = blobToDataURL(WAV_audio);
    recorder.play(audio);
    // uploadAudio();
}

function playRecording() {
    recorder.play(audio);
}

function uploadAudio() {
    recorder.upload("http://127.0.0.1:8000", function (state, e) {
        switch (state) {
            case 'uploading':
                //var percentComplete = Math.round(e.loaded * 100 / e.total) + '%';
                break;
            case 'ok':
                //alert(e.target.responseText);
                //alert("上传成功");
                window.location.href = "http://127.0.0.1:8000";
                break;
            case 'error':
                alert("上传失败");
                break;
            case 'cancel':
                alert("上传被取消");
                break;
        }
    });
}





// // json格式化
// var url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_asr';//api地址
// var data = {
//     'app_id': '2117697213',//应用ID
//     'format': '2',//WAV格式的编号
//     'rate': '16000',//采样率
//     'speech': 'audio',//base64的音频
//     'time_stamp': 'time',//音频的持续时间 秒级时间戳
//     'nonce_str': 'fa577ce340859f9fe',//未知
//     'sign': '',//数字签名
// };//必要数据字典

// function getReqSign() {
//     alert(WAV_audio);
// }