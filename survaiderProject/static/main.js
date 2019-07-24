



var conf={
    malecount:0,
    femalecount:0

}
firstcomponent=Vue.extend({
    template:`<h1>first comonent working</h1>`,



});

secondcomp=Vue.extend({

    template:`<h2>this is second comp</h2>`,

});
homecomponent=Vue.extend({
    template:"#home",
    components: {
        apexchart: VueApexCharts,
      },
    data(){
        return{

            x:2111,
            y:700,
            series: [conf.malecount,conf.femalecount],
            chartOptions: {
              labels: ['Male', 'Female',],
              responsive: [{
                breakpoint: 480,
                options: {
                  chart: {
                    width: 200
                  },
                  legend: {
                    position: 'bottom'
                  }
                }
              }]
            },


            ls:['akhil','shukla'],

        }

    },
    beforeCreate(){

        this.$http.get('http://127.0.0.1:8000/app/malecount/')
        .then((response)=>{
        conf.malecount=JSON.parse(response.data['malecount']);
        conf.femalecount=JSON.parse(response.data['femalecount']);

        console.log(conf.malecount);
         console.log(conf.femalecount);
            this.series=[conf.malecount,conf.femalecount];

        });






    },
});
routes=[
    {
        path:'/',
        component:homecomponent

    },
    {
        path:'/first',
        component:firstcomponent

    },
    {
        path:'/secondcomp',
        component:secondcomp
    }


]

const router=new VueRouter({routes});

new Vue({router}).$mount("#app");
