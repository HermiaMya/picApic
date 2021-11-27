<template>
  <div class="q-pa-md" >
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
          <q-tab name="mails" label="表情包" />
          <q-tab name="alarms" label="多IP联动" />
          <q-tab name="movies" label="AI换脸" />
        </q-tabs>

        <q-tab-panels v-model="tab" animated class="bg-primary text-white">
          <q-tab-panel name="mails">
            <q-img
              src="https://i.loli.net/2021/11/25/WPAU3iMwQGsZ9Oj.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://i.loli.net/2021/11/25/lrS3NR6Z8P7i4LC.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://i.loli.net/2021/11/26/ePQBtmRw2HU1J7a.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://i.loli.net/2021/11/26/rKXtIjnfFPvWLYx.gif"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
            />
            <q-img
              src="https://i.loli.net/2021/11/26/jWDFoYUBrzsJSuA.jpg"
              spinner-color="white"
              style="height: 140px; max-width: 150px"
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
      tab: 'mails'
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
.q-panel > div {
    height: 100%;
    width: 300%;
}
</style>