 $(function(){
        set_endpoint('http://140.113.199.198:9992');
		set_PUSH_INTERVAL(500);

        var profile = {
		    'dm_name': 'DM_0416213',
			'idf_list':[['None']],
			'odf_list':[[odf_0416213,['None']]],
        };

        function Dummy_Sensor(){
            return Math.random();
        }

        function Dummy_Control(data){
            $('.ODF_value')[0].innerText=data[0];
        }

        function odf_0416213(data)
        {
            $('.ODF_value')[0].innerText=data[0];
        }

/*******************************************************************/
        function ida_init(){console.log('Success.');}
        var ida = {
            'ida_init': ida_init,
        };
        dai(profile,ida);
});
