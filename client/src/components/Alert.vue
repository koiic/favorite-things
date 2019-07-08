<template>
  <div>
    <b-alert v-mode="true" :variant="variant" show dismissible>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message', 'variant'],
};
</script>
