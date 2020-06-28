<template>
  <div>
    <v-row>
      <v-col cols="12">
        <h2 class="message-title">
          Discover
        </h2>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="9">
        <div v-for="discover in DiscoverList" :key="discover.id">
          <AccordionForDiscover>
            <div slot="source">{{ discover.source }}</div>
            <div slot="header">
              {{ discover.title }}
            </div>
            <div slot="body">
              {{ discover.main }}
            </div>
          </AccordionForDiscover>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import AccordionForDiscover from "./AccordionForDiscover.vue";

export default {
  components: {
    AccordionForDiscover,
  },
  data: function() {
    return {
      DiscoverList: [
        {
          main:
            "<h1>React</h1>React and Vue share many similarities. They both:<p>・utilize a virtual DOM</p><p>・provide reactive and composable view components</p><p>・maintain focus in the</p>core library, with concerns such as routing 　and global state management handled by companion libraries Being so similar in scope, we’ve put more time into fine-tuning this comparison than any other. We want to ensure not only technical accuracy, but also balance. We point out where React  outshines Vue, for example in the richness of their ecosystem and abundance of their custom renderers. With that said, it’s inevitable that the comparison would appear biased towards Vue to some React users, as many of the subjects explored are to some extent subjective. We acknowledge the existence of varying technical taste, and this comparison primarily aims to outline the reasons why Vue could potentially be a better fit if your preferences happen to coincide with ours. Some of the sections below may also be slightly outdated due to recent updates in React 16+, and we are planning to work with the React community to revamp this section in the near future.",
          title: "Hello World",
          source: "@countermeasure#44",
        },
        {
          main:
            "<h1>React</h1>React and Vue share many similarities. They both:<p>・utilize a virtual DOM</p><p>・provide reactive and composable view components</p><p>・maintain focus in the</p>core library, with concerns such as routing 　and global state management handled by companion libraries Being so similar in scope, we’ve put more time into fine-tuning this comparison than any other. We want to ensure not only technical accuracy, but also balance. We point out where React  outshines Vue, for example in the richness of their ecosystem and abundance of their custom renderers. With that said, it’s inevitable that the comparison would appear biased towards Vue to some React users, as many of the subjects explored are to some extent subjective. We acknowledge the existence of varying technical taste, and this comparison primarily aims to outline the reasons why Vue could potentially be a better fit if your preferences happen to coincide with ours. Some of the sections below may also be slightly outdated due to recent updates in React 16+, and we are planning to work with the React community to revamp this section in the near future.",
          title: "How to use the Django Rest Fwamework.",
          source: "",
        },
        {
          main:
            "<h1>React</h1>React and Vue share many similarities. They both:<p>・utilize a virtual DOM</p><p>・provide reactive and composable view components</p><p>・maintain focus in the</p>core library, with concerns such as routing 　and global state management handled by companion libraries Being so similar in scope, we’ve put more time into fine-tuning this comparison than any other. We want to ensure not only technical accuracy, but also balance. We point out where React  outshines Vue, for example in the richness of their ecosystem and abundance of their custom renderers. With that said, it’s inevitable that the comparison would appear biased towards Vue to some React users, as many of the subjects explored are to some extent subjective. We acknowledge the existence of varying technical taste, and this comparison primarily aims to outline the reasons why Vue could potentially be a better fit if your preferences happen to coincide with ours. Some of the sections below may also be slightly outdated due to recent updates in React 16+, and we are planning to work with the React community to revamp this section in the near future.",
          title:
            "Post of API on Django database to sort order by Draggable of Vue.js use the Django Rest Fwamework. Post of API on Django database to sort order by Draggable of Vue.js use the Django Rest Fwamework.",
          source: "@motivation#2",
        },
        {
          main:
            "<h1>React</h1>React and Vue share many similarities. They both:<p>・utilize a virtual DOM</p><p>・provide reactive and composable view components</p><p>・maintain focus in the</p>core library, with concerns such as routing 　and global state management handled by companion libraries Being so similar in scope, we’ve put more time into fine-tuning this comparison than any other. We want to ensure not only technical accuracy, but also balance. We point out where React  outshines Vue, for example in the richness of their ecosystem and abundance of their custom renderers. With that said, it’s inevitable that the comparison would appear biased towards Vue to some React users, as many of the subjects explored are to some extent subjective. We acknowledge the existence of varying technical taste, and this comparison primarily aims to outline the reasons why Vue could potentially be a better fit if your preferences happen to coincide with ours. Some of the sections below may also be slightly outdated due to recent updates in React 16+, and we are planning to work with the React community to revamp this section in the near future.",
          title: "Hello World",
        },
      ],
    };
  },
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            Font Desiign
 -----------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  /* font-size: 34px; */
  line-height: 40px;
  color: #088dda;
  font-size: 34px;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 40px;
  color: #4d4d4d;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  /* line-height: 1.6; */
  /* letter-spacing: 0.05em; */
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}

.content-splitter {
  border-block-end: solid 1px #c5c5c5;
  /* padding-bottom: 5px; */
}
</style>
