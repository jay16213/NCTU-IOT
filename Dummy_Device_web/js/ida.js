 $(function(){
        csmapi.set_endpoint ('http://140.113.199.204:9999');
        var profile = {
            'dm_name': '0416213',
            'idf_list':[Dummy_Sensor],
            'odf_list':[js_0416213_ODF],
        };

        var last_state = 0;
        var state = 0;

        function Dummy_Sensor(){
            return Math.random();
        }

        function Dummy_Control(data){
            $('.ODF_value')[0].innerText=data[0];
        }

        function js_0416213_ODF(data) {
            last_state = state;
            if(data[0] >= 0)
                $('.ODF_value')[0].innerText="smart phone is up";
            else
                $('.ODF_value')[0].innerText="smart phone is down";


            // if(last_state != state) {
            //     if(state == 1) {
            //         console.log("up");
            //     }
            //     else {
            //         console.log("down");
            //     }
            // }
            // $('.ODF_value')[0].innerText=data[0];
        }

/*******************************************************************/
        function ida_init(){}
        var ida = {
            'ida_init': ida_init,
        };
        dai(profile,ida);
});
