<template>
  <div id="app">
    <div id="header">
      <v-app-bar justify="space-around">
        <v-btn>Carousell</v-btn>
        <v-text-field hide-details prepend-icon='mdi-magnify'>
        </v-text-field>
        <v-btn class="ma-2" color="red" dark to="/listings">
          SELL
          
          <v-icon dark right> mdi-sale </v-icon>
        </v-btn>
      </v-app-bar>
    </div>
    <stack
      :column-min-width="300"
      :gutter-width="15"
      :gutter-height="15"
      monitor-images-loadedgit 
    >
    <stack-item 
      v-for="(item, i) in images" :key="i" class="img-container" >
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
  async mounted() { 
    const listings = await this.$axios.$get('/api/users/feed/?limit=20')
    this.images = listings.listings.map(x => x.images).map(y => y.filename)
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

