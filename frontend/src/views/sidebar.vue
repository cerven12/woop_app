<template>
  <div id="sidebar">
    <v-list rounded color="#f7f7f7" flat>
      <v-subheader>REPORTS</v-subheader>
      <v-list-item-group v-model="item" color="primary">
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-icon>
            <!-- <v-icon v-text="item.icon"></v-icon> -->
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
export default {
  data: () => ({
    item: 1,
    items: [
      { text: "Goal", icon: "mdi-clock" },
      { text: "My Calendar", icon: "mdi-account" },
      { text: "Notes", icon: "mdi-flag" },
    ],
  }),
};
</script>

<style scoped>
#sidebar {
  margin: 10px;
  background: rgb(247, 247, 247);
}
</style>
