export default {
    name: 'Host',
    
    data () {
      return {
        msg: '主机异常',
        modal:false,
        title1:'当前异常(5)',
        title2:'Top10 CPU',
        title3:'Top10 硬盘空间利用率',
        title4:'Top10 内存',
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
            {
                title: '时间',
                key: 'date'
            }
        ],
        data1: [
            {
                name: '1',
                age: '10.7.9.12',
                address: '钦州路',
                effect: '计费',
                error:' 磁盘IO过高',
                date: '2016-10-03'
            },
            {
                name: '2',
                age: '10.7.9.2',
                address: '新黄埔',
                effect: '计费',
                error:' CPU占用过高',
                date: '2016-10-03'
            },
            {
                name: '3',
                age: '11.7.9.12',
                address: '钦州路',
                effect: '客服',
                error:' 磁盘IO过高',
                date: '2016-10-03'
            },
            {
                name: '4',
                age: '15.7.9.12',
                address: '新黄埔',
                effect: '营收',
                error:' CPU占用过高',
                date: '2016-10-03'
            },
            
        ],

        columns2: [
            
            {
                title: 'IP',
                key: 'ip'
            },
            {
                title: '主机名',
                key: 'name'
            },
            {
                title: 'CPU',
                key: 'CPU'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data2: [
            {
                ip: '10.7.9.12',
                name: '',
                CPU:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                CPU:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                CPU:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                CPU:' 99%',
                address: '钦州路',
            }
        ],

        columns3: [
            
            {
                title: 'IP',
                key: 'ip'
            },
            {
                title: '主机名',
                key: 'name'
            },
            {
                title: '磁盘空间',
                key: 'space'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data3: [
            {
                ip: '10.7.9.12',
                name: '',
                space:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                space:' 19%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                space:' 9%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                space:' 99%',
                address: '钦州路',
            }
        ],

        columns4: [
            
            {
                title: 'IP',
                key: 'ip'
            },
            {
                title: '主机名',
                key: 'name'
            },
            {
                title: '内存利用率',
                key: 'ram'
            },
            {
                title: '机房',
                key: 'address'
            }
        ],
        data4: [
            {
                ip: '10.7.9.12',
                name: '',
                ram:' 99%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                ram:' 19%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                ram:' 9%',
                address: '钦州路',
            },
            {
                ip: '10.7.9.12',
                name: '',
                ram:' 99%',
                address: '钦州路',
            }
        ],
        columns5: [
            
            {
                title: '网卡名称',
                key: 'title'
            },
            {
                title: '出速率',
                key: 'outSpeed'
            },
            {
                title: '入速率',
                key: 'inSpeed'
            },
           
        ],
        data5: [
            {
                title: '网卡1',
                outSpeed:' 1 MB/s',
                inSpeed: '2 MB/s',
            },
            {
                title: '网卡2',
                outSpeed:' 1 MB/s',
                inSpeed: '2 MB/s',
            },
            {
                title: '网卡3',
                outSpeed:' 1 MB/s',
                inSpeed: '2 MB/s',
            },
           
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