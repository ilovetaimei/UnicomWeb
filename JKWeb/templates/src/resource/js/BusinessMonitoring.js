import Queen  from '@/components/Queen.vue'
import 'iview/dist/styles/iview.css'
import axios from 'axios'
import API from '../../api/API';
import baseConfig from '../../api/config'
const api = new API();


export default {
    name: 'BusinessMonitoring',
    components:{
        Queen,
      },
    //   props:{
    //     modal1:{
    //         default:false
    //     }
    //   },
    data () {
      return {
        baseURL: baseConfig.baseURL,
        modal1:false,
        maskIsShow: false,
        coverIsShow:false,
        msg: '业务监控',
        title1:'计费业务',
        screenWidth:1800,
        num1:'子业务1',
        num2:'子业务2',
        num3:'子业务3',
        num4:'子业务4',
        num5:'子业务5',
        colorChange: true
      }
    },

    methods:{   

        init:function(){
            this.iniData();
        },
        iniData:function(){
            console.log(this.baseURL)
            api.myPost('/jk').then((res)=>{
                        console.log(res)
                },(err)=>{
                     console.log('iniData'  + err);
                })

        },

        ok () {
            this.$Message.info('Clicked ok');
        },
        cancel () {
            this.$Message.info('Clicked cancel');
        },
        changeColor:function(){
            var num1 = document.getElementsByClassName('num1')[0];
            num1.style.background = "red";
            num1.style.color = "white";
        },

        //绘制结构
        drawBlockBg: function () {
            this.drawBlock1();
            this.drawBlock2();
            this.drawBlock3();
            this.drawBlock4();
            // this.drawcircularFont();
          },

        drawBlock1: function(){
            let dom = document.getElementsByClassName('treeOne')[0];
            var ctx1 = dom.getContext('2d');
            ctx1.clearRect(0, 0, 800, 320);
            ctx1.beginPath();
            ctx1.lineWidth = 2;
            ctx1.strokeStyle = '#365f98'; 

             // 直线边界
            ctx1.save();
            ctx1.beginPath();
            ctx1.moveTo(400, 0);
            ctx1.lineTo(400, 60);
            ctx1.lineTo(80, 60);
            ctx1.lineTo(80, 120);

            ctx1.moveTo(400, 60);
            ctx1.lineTo(700, 60);
            ctx1.lineTo(700, 120);

            ctx1.moveTo(210, 60);
            ctx1.lineTo(210, 180);
            ctx1.lineTo(160, 180);
            ctx1.lineTo(160, 250);

            ctx1.moveTo(320, 60);
            ctx1.lineTo(320, 120);

            ctx1.moveTo(520, 60);
            ctx1.lineTo(520, 180);
            ctx1.lineTo(620, 180);
            ctx1.lineTo(620, 240);
            
            ctx1.stroke();
            ctx1.closePath();
            ctx1.restore();

            // // 弧形边界
            // ctx1.save();
            // ctx1.beginPath();
            // ctx1.lineWidth = 4;
            // ctx1.strokeStyle = '#365f98';
            // ctx1.fillStyle = 'rgba(242, 242, 242, 1)';
            // ctx1.moveTo(60, 70);
            // ctx1.arc(60, 70, 8, 0, 2*Math.PI, false);
            // ctx1.stroke();

            // ctx1.fill();
            // ctx1.closePath();
            // ctx1.restore();

        },
        drawBlock2: function(){
            let dom = document.getElementsByClassName('treeTwo')[0];
            var ctx1 = dom.getContext('2d');
            ctx1.clearRect(0, 0, 800, 320);
            ctx1.beginPath();
            ctx1.lineWidth = 2;
            ctx1.strokeStyle = '#365f98'; 
             // 直线边界
            ctx1.save();
            ctx1.beginPath();
            ctx1.moveTo(400, 0);
            ctx1.lineTo(400, 60);
            ctx1.lineTo(80, 60);
            ctx1.lineTo(80, 120);
            ctx1.moveTo(400, 60);
            ctx1.lineTo(700, 60);
            ctx1.lineTo(700, 120);
            ctx1.moveTo(210, 60);
            ctx1.lineTo(210, 180);
            ctx1.lineTo(160, 180);
            ctx1.lineTo(160, 250);
            ctx1.moveTo(320, 60);
            ctx1.lineTo(320, 120);
            ctx1.moveTo(520, 60);
            ctx1.lineTo(520, 180);
            ctx1.lineTo(620, 180);
            ctx1.lineTo(620, 240);
            ctx1.stroke();
            ctx1.closePath();
            ctx1.restore();
        },
        drawBlock3: function(){
            let dom = document.getElementsByClassName('treeThree')[0];
            var ctx1 = dom.getContext('2d');
            ctx1.clearRect(0, 0, 800, 320);
            ctx1.beginPath();
            ctx1.lineWidth = 2;
            ctx1.strokeStyle = '#365f98'; 
             // 直线边界
            ctx1.save();
            ctx1.beginPath();
            ctx1.moveTo(400, 0);
            ctx1.lineTo(400, 60);
            ctx1.lineTo(80, 60);
            ctx1.lineTo(80, 120);
            ctx1.moveTo(400, 60);
            ctx1.lineTo(700, 60);
            ctx1.lineTo(700, 120);
            ctx1.moveTo(210, 60);
            ctx1.lineTo(210, 180);
            ctx1.lineTo(160, 180);
            ctx1.lineTo(160, 250);
            ctx1.moveTo(320, 60);
            ctx1.lineTo(320, 120);
            ctx1.moveTo(520, 60);
            ctx1.lineTo(520, 180);
            ctx1.lineTo(620, 180);
            ctx1.lineTo(620, 240);
            ctx1.stroke();
            ctx1.closePath();
            ctx1.restore();
        },
        drawBlock4: function(){
            let dom = document.getElementsByClassName('treeFour')[0];
            var ctx1 = dom.getContext('2d');
            ctx1.clearRect(0, 0, 800, 320);
            ctx1.beginPath();
            ctx1.lineWidth = 2;
            ctx1.strokeStyle = '#365f98'; 
             // 直线边界
            ctx1.save();
            ctx1.beginPath();
            ctx1.moveTo(400, 0);
            ctx1.lineTo(400, 60);
            ctx1.lineTo(80, 60);
            ctx1.lineTo(80, 120);
            ctx1.moveTo(400, 60);
            ctx1.lineTo(700, 60);
            ctx1.lineTo(700, 120);
            ctx1.moveTo(210, 60);
            ctx1.lineTo(210, 180);
            ctx1.lineTo(160, 180);
            ctx1.lineTo(160, 250);
            ctx1.moveTo(320, 60);
            ctx1.lineTo(320, 120);
            ctx1.moveTo(520, 60);
            ctx1.lineTo(520, 180);
            ctx1.lineTo(620, 180);
            ctx1.lineTo(620, 240);
            ctx1.stroke();
            ctx1.closePath();
            ctx1.restore();
        },
        showCover:function(){
            // this.modal1 = true;
            this.coverIsShow = true;
            this.maskIsShow = true;
        },
        cancel:function(){
            this.maskIsShow = false;
            this.coverIsShow = false;
        },
        mask:function(){   //遮罩层背景完全覆盖 网页
            var hh = window.screen.height + 100 ;
            var mask = document.getElementById("mask");
            if(mask){
                mask.style.height = hh + 'px';
                mask.style.width =   '1830px';
            }else{
                return;
            }
        },

        handleResize:function (){    //缩放页面的大小
            window.screenWidth = document.body.clientWidth ;
            this.screenWidth = window.screenWidth;
            let scaleSize = this.screenWidth/1800;
            for(var i = 0;i<document.getElementsByClassName('container').length;i++){
              document.getElementsByClassName('container')[i].style.WebkitTransform = "scale("+scaleSize+")";
            }
        },
    },

    mounted(){
        this.init();
        this.changeColor();
        this.drawBlockBg();
        this.handleResize();
        window.addEventListener('resize',this.handleResize);
    }
  }