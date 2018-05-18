$(function () {
    set_endpoint('http://140.113.199.198:9992');
    set_PUSH_INTERVAL(500);

    var profile = {
        'dm_name': 'Bulb',
        'idf_list': [],
        'odf_list': [[Color_O, ['None']], [Luminance, ['None']]]
    }

    var r = 255;
    var g = 255;
    var b = 0;
    var lum = 100;

    function draw () {
        var rr = Math.floor((r * lum) / 100);
        var gg = Math.floor((g * lum) / 100);
        var bb = Math.floor((b * lum) / 100);
        $('.bulb-top, .bulb-middle-1, .bulb-middle-2, .bulb-middle-3, .bulb-bottom, .night').css(
            {'background': 'rgb('+ rr +', '+ gg +', '+ bb +')'}
        );
    }

    function Color_O(data) {
        console.log(data[0]);
        r = data[0];
        g = data[1];
        b = data[2];
        draw();
    }

    function Luminance(data) {
        console.log(data);
        lum = data[0];
        draw();
    }

    /*******************************************************************/
    function ida_init(){console.log('Success.');}
    var ida = {
        'ida_init': ida_init,
    };

    dai(profile,ida);

    $('font')[0].innerText = profile['name']; //profile['name'];
    lum = 255;
    draw();
});
