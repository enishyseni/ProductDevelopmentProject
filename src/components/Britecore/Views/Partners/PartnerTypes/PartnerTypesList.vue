<template>

<div class="row">
<div class="col-md-6 col-xs-12">
  <div v-for="(value, key, index) in collection" class="card" v-on:click="select(value)" :value="value.id" style="cursor: pointer;">
    <div class="header">
      <h4 class="title">{{value.Name}}</h4>
    </div>

    <div class="content">
        <div class="row">
          <div class="col-md-12 col-xs-12">
                  
                   {{value.Description}} 
                  
          </div>
          <div class="col-md-12 col-xs-12">
                  <div class="row">
                    <div class="col-md-offset-9 col-md-3 col-xs-12">
                      {{value.CreatedDate}} 
                    </div>
                   </div>                  
          </div>
          
        </div>
        <div class="clearfix"></div>   
      </div>        
    
    </div>
  </div>

  <div v-if="selected !== null" class="col-md-6 col-xs-12">
  <div class="card">
    <div class="header">
      <h4 class="title">{{selected.Name}}</h4>
    </div>

    <div class="content">
        <div class="row">
          <div class="col-md-12 col-xs-12">
                  
                   {{selected.Description}} 
                  
          </div>
          <div class="col-md-12 col-xs-12">
                  
                   {{selected.CreatedDate}} 
                  
          </div>
          
        </div>
        <div class="clearfix"></div>   
      </div>        
    
    </div>
  </div>

<div v-if="selected === null" class="col-md-6 col-xs-12">
  <div class="row">
    <div class="col-md-offset-2 col-md-8 col-md-offset-2"><h3>Click on the list for details to be shown here.</h3></div>
  </div>
</div>



</div>

</template>

<script>
import PartnerService from "../../../../../common/api.service";
import store from '@/store'
import { CHECK_AUTH } from '@/store/actions.type'

export default {
  data() {
    return {
      collection: [], //[{"aaa": "bbb"}, {"aaa": "bbb"}, {"aaa": "bbb"}, {"aaa": "bbb"}, {"aaa": "bbb"}, {"aaa": "bbb"}]
      selected: null
    };
  },
  methods: {
    fillCollection() {
      store.dispatch(CHECK_AUTH)
      let that = this;
      PartnerService.query("partnertypes").then(response => {
        that.collection = response.data;
        //that.$forceUpdate();
        console.log(that.collection);
      });
    },
    select(value) {
      store.dispatch(CHECK_AUTH)
      console.log('Selected ID: ' + value.id)
      let that = this;
      PartnerService.get("partnertype", value.id).then(response => {
        that.selected = response.data;
        console.log(that.selected);
      });
    }
  },
  mounted() {
    this.fillCollection();
    console.log(this.collection);
  }
};
</script>
<style>
</style>
