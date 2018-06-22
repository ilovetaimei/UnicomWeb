<template>
  <Carousel :autoplay="isAutoplay" :autoplay-speed="40000"  v-model="value2"  id="carouselMain"  height = "1068px">
        <CarouselItem>
            <div>
              <BusinessMonitoring ></BusinessMonitoring>
            </div>
        </CarouselItem>

        <CarouselItem>
            <div>
              <Host ></Host>
            </div>
        </CarouselItem>

        <CarouselItem>
          <div>
            <Net></Net>
          </div>
        </CarouselItem>
        
   </Carousel>
</template>

<script>
import Host from './Host'
import Net from './Net'
import BusinessMonitoring from './BusinessMonitoring'
import 'iview/dist/styles/iview.css';
export default {
  name:'mainframe',
  components:{
    Host,
    BusinessMonitoring,
    Net,
  },

 data () {
            return {
                isAutoplay:true,
                value2: 0,
                cunIndex:0,
            
            }
        },
  methods:{
  },

  mounted(){
  }

}
</script>




