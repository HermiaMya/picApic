<template>
  <div class="all">
    <div :style="conTop"></div>
    <q-layout view="hHh LpR fFf">
      <q-header bordered class="bg-primary text-white" height-hint="98">
        <q-tabs align="center">
          <q-route-tab to="/page1" label="表情包" />
          <q-route-tab to="/page2" label="智能优化" />
          <q-route-tab to="/page3" label="卡通形象" />
          <q-route-tab to="/page4" label="精准修图" />
        </q-tabs>
      </q-header>
      <q-page-container>
        <router-view />
      </q-page-container>
    </q-layout>
  </div>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue';

const linksData = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
];

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData,
      conTop: {
        backgroundImage: 'url(' + require('../picture/back.jpg') + ')',
        backgroundRepeat: 'no-repeat',
      },
    }
  },
}
</script>
<style scoped>
.all {
  background: "~picture/back.jpg";
}
.bg-primary {
    background: none !important;
    background: none !important;
}
</style>
