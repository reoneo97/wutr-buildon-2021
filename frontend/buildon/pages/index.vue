<template>
  <div id="app">
    <stack
      :column-min-width="300"
      :gutter-width="15"
      :gutter-height="15"
      monitor-images-loadedgit
    >
    <stack-item
      v-for="(item, i) in images" :key="i" class="img-container" to="/view" @click="viewItem(item)">
        <img :src="`https://wutr-images2.s3.ap-southeast-1.amazonaws.com/${item}`" />
<!-- 
https://wutr-images2.s3.ap-southeast-1.amazonaws.com/02af94fcf13d11ebb2730242c0a83003.jpeg
This is to get the images based on the URL link
<div v-for="(data, key) in imgURL" :key="key">
  <img :src= "getLink(data)" />
</div> 

This is to be exported and replaced with data instead.
  methods: {
     async getLink(url){
      let response = await PostsService.downloadURL({
        imgURL : url
      })
      //return response.data
      let imgdata = await axios.get(response.data)
      console.log(imgdata.data)
      return imgdata.data
     }
  }
  
  --> 

      </stack-item>
    </stack>
  </div>
</template>

<script>
// import axios from "axios";
export default {
  components: {},
  
  data() {
    return {
      images: [],
    };
  },
  methods: {
    viewItem(item) {
      const index = item.indexOf('.')
      this.$emit('update-itemName', item.slice(0, index))
    }
  },
  async mounted() {
    // const URL = 'http://wutr-staging.eba-jy7d9spr.ap-southeast-1.elasticbeanstalk.com/api/users/feed?limit=20'
    const URL = '/api/users/feed/?limit=20'
    const listings = await this.$axios.$get(URL)
    // console.log(listings)
    console.log(listings.listings)
    this.images = listings.listings.map(x => x.filename)
    }
  };
  </script>
  <!--


  methods: {
    async getLink(url){
    let response = await PostsService.downloadURL({
      imgURL : url
    })
    //return response.data
    let imgdata = await axios.get(response.data)
    console.log(imgdata.data)
    return imgdata.data
  }
  }
  -->



<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.img-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: center;
  overflow: hidden;
  margin: 0;
  object-fit: fill;
  cursor: pointer;
}
.img-container img {
  display: block;
  margin: 0;
  width: 100%;
  height: auto;
}
.img-container figcaption {
  margin: 3px 0;
  text-align: center;
}

.header {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  padding: 20px 20px;
}
</style>

