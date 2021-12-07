<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md" style="max-width: 600px">
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="bg-pink-1 text-grey-7"
          active-color="primary"
          indicator-color="purple"
          align="justify"
        >
          <q-tab name="3-1" label="动漫脸" />
          <q-tab name="3-2" label="字符画" />
          <q-tab name="3-3" label="像素画" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="bg-primary text-white">
          <q-tab-panel name="mails">
            <q-img
              src="https://i.loli.net/2021/11/26/3wckgSQo6DXHGzm.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 210px"
            />
            <q-img
              src="https://i.loli.net/2021/11/26/xnNhG13SciefElI.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 210px"
            />
          </q-tab-panel>

          <q-tab-panel name="alarms">
            <q-img
              src="https://i.loli.net/2021/11/26/woV1Q5HBzqFChZu.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://i.loli.net/2021/11/26/GWM38kB7IENyiSU.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
          </q-tab-panel>

          <q-tab-panel name="movies">
            <q-img
              src="https://i.loli.net/2021/11/26/4RykKnvgwhBboXi.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://i.loli.net/2021/11/26/Vo8IlULtAhyGPap.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tab: '3-1'
    }
  },
  methods:{
         sendMsg(){
             //func: 是父组件指定的传数据绑定的函数，this.msg:子组件给父组件传递的数据
             this.$emit('func',this.tab)
         }
     }
}
</script>

<style>
.bg-primary {
    background:rgb(234,184,219) !important;
}
.q-tab-panel {
    padding: 30px;
}
.absolute-full, .fullscreen, .fixed-full {
    top: 0px;
    right: 4px;
    bottom: 0;
    left: 4px;
}
</style>