import Queen  from '@/components/Queen.vue'
import 'iview/dist/styles/iview.css'

export default {
    name: 'test',
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
        modal1:true,
        msg: '业务监控',
        title1:'计费业务',
      }
    },

    methods:{   
        ok () {
            this.$Message.info('Clicked ok');
        },
        cancel () {
            this.$Message.info('Clicked cancel');
        },
     
        showCover:function(){
            this.modal1 =  !this.modal1;
            this.coverIsShow = true;
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
        this.handleResize();
        window.addEventListener('resize',this.handleResize);
    }
  }