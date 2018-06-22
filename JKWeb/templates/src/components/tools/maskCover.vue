<template>
    <!-- <Button type="primary" @click="modal1 = true">Display dialog box</Button> -->
    <Modal
        v-model="modal1"
        title="Common Modal dialog box title"
        @on-ok="ok"
        @on-cancel="cancel">
        <p>Content of dialog</p>
        <p>Content of dialog</p>
        <p>Content of dialog</p>
    </Modal>
</template>
<script>
    export default {
        name: 'maskCover',
         props:{
            modal1:{
                type:Boolean,
                default:false
            }
        },
        data () {
            return {
                // modal1: this.isShow
            }
        },
        methods: {
           
            ok () {
                this.$Message.info('Clicked ok');
            },
            cancel () {
                this.$Message.info('Clicked cancel');
            }
        },
        mounted:{
           
        }
    }
</script>
