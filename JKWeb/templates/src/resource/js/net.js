export default {
    name: 'Net',
    
    data () {
      return {
        msg: '主机异常',
        modal:false,
        title1:'当前异常(5)',
        title2:'Top10 延迟',
        title3:'Top10 丢包率',
        title4:'Top10 错误包数量',
        title5:'Top10 端口利用率',
        cpuNum:'60%',
        ramNum:'50%',
        diskNum:'10mbps',
        diskRate:'磁盘1（95%）  磁盘2（40%）',
        netDelay:'10ms',
        columns1: [
            {
                title: '序号',
                key: 'name'
            },
            {
                title: 'IP',
                key: 'age'
            },
            {
                title: '机房',
                key: 'address'
            },
            {
                title: '影响业务',
                key: 'effect'
            },
            {
                title: '故障描述',
                key: 'error'
            },
           
        ],
        data1: [
            {
                name: '1',
                age: '10.7.9.12',
                address: '钦州路',
                effect: '计费',
                error:' 磁盘IO过高',
            },
            {
                name: '2',
                age: '10.7.9.2',
                address: '新黄埔',
                effect: '计费',
                error:' CPU占用过高',
            },
            {
                name: '3',
                age: '11.7.9.12',
                address: '钦州路',
                effect: '客服',
                error:' 磁盘IO过高',
            },
            {
                name: '4',
                age: '15.7.9.12',
                address: '新黄埔',
                effect: '营收',
                error:' CPU占用过高',
            },
            
        ],

        columns2: [
            
            {
                title: 'IP',
                key: 'ip'
            },
          
            {
                title: '延迟',
                key: 'delay'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data2: [
            {
                ip: '10.7.9.12',
                delay:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                delay:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                delay:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                delay:' 99%',
                address: '钦州路',
            }
        ],

        columns3: [
            
            {
                title: 'IP',
                key: 'ip'
            },
            
            {
                title: '丢包率',
                key: 'lost'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data3: [
            {
                ip: '10.7.9.12',
                lost:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                lost:' 19%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                lost:' 9%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                lost:' 99%',
                address: '钦州路',
            }
        ],

        columns4: [
            
            {
                title: 'IP',
                key: 'ip'
            },
            
            {
                title: '错误包数量',
                key: 'err'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data4: [
            {
                ip: '10.7.9.12',
                err:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                err:' 19%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                err:' 9%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                err:' 99%',
                address: '钦州路',
            }
        ],
        columns5: [
            
            {
                title: 'IP',
                key: 'ip'
            },
            
            {
                title: '端口利用率',
                key: 'use'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data5: [
            {
                ip: '10.7.9.12',
                use:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                use:' 19%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                use:' 9%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                use:' 99%',
                address: '钦州路',
            }
        ],
      }
    },
    methods:{
        ok () {
            this.$Message.info('Clicked ok');
        },
        cancel () {
            this.$Message.info('Clicked cancel');
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