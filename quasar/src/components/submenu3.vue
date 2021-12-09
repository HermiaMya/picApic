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
          <q-tab name="carton" label="动漫脸" />
          <q-tab name="pix" label="像素画" />
          <q-tab name="char" label="字符画" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="bg-primary text-white">
          <q-tab-panel name="carton">
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

          <q-tab-panel name="pix">
            <q-form @submit="onSubmit" class="q-gutter-md">
            <div class="slide" style="float:left">
              <q-badge color="blue-4">
                像素格尺寸:小-->大
              </q-badge>
              <q-slider
              v-model="value"
              :min="4"
              :max="8"
              :step="0.1"
              label
              color="blue-4"
              />
              <div>
                <q-btn class="button1" label="确定" type="submit"></q-btn>
              </div>
            </div>
            </q-form>
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

          <q-tab-panel name="char">
            <q-form @submit="onSubmit" class="q-gutter-md">
            <div class="slide" style="float:left">
              <q-badge color="blue-4">
                字符密度:稀-->密
              </q-badge>
              <q-slider
              v-model="value"
              :min="4"
              :max="8"
              :step="0.1"
              label
              color="blue-4"
              />
              <div>
                <q-btn class="button1" label="确定" type="submit"></q-btn>
              </div>
            </div>
            </q-form>
            <q-img
              src="https://s2.loli.net/2021/12/09/p5Pl7FOwGvRxHMQ.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://s2.loli.net/2021/12/09/xKgRzms2JXfc9Hq.jpg"
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
import submenu1Vue from './submenu1.vue'
export default {
  data () {
    return {
      tab: 'carton',
      submitResult: ""
    }
  },
  methods:{
         sendMsg(){
             //func: 是父组件指定的传数据绑定的函数，this.msg:子组件给父组件传递的数据
             this.$emit('func',this.tab)
             this.$emit('size',this.submitResult)
         },
         onSubmit (evt) {
            const formData = new FormData(evt.target)
            const submitResult = ""

            for (const value of formData.entries()) {
            submitResult = value
            }

          this.submitResult = submitResult
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
.slide{
  padding: 0px 20px;
  margin-top: 40px;
  width: 180px;
}
.button1{
  background-color:RGB(100,181,246);
}
</style>