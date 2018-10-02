<template>
<div class="row">
<div class="col-md-6 col-xs-12">
  <div class="card">
    <div class="header">
      <h4 class="title">Add or select partner</h4>
    </div>
    <div class="content">
      <form>

        <div class="row">

          <div class="col-md-12 col-xs-12">
            <fg-input type="text"
                      label="Name (Partner Member)"
                      placeholder="Name of type"
                      v-model="partnerType.Name">
            </fg-input>
          </div>

          <div class="col-md-12 col-xs-12">
            <fg-input type="text"
                      label="Lastname (Partner Member)"
                      placeholder="Name of type"
                      v-model="partnerType.Name">
            </fg-input>
          </div>


          <div class="col-md-12 col-xs-12">
            <fg-input type="text"
                      label="Name"
                      placeholder="Name of type"
                      v-model="partnerType.Name">
            </fg-input>
          </div>



          <div class="col-md-12 col-xs-12">
            <div class="form-group">
              <label style="margin-left: 10px;">Description (Partner Member)</label>
              <textarea style="margin-left: 10px;"
                        class="form-control border-input"
                        placeholder="Description of type"
                        v-model="partnerType.Description">
              </textarea>
            </div>
          </div>        
        </div>

        <div class="row">
        <div class="text-center">
          <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="saveModel">
            Save
          </button>
        </div>
        </div>

        <div class="clearfix"></div>
        </form>
      </div>        
    
    </div>
  </div>

<div v-if="selected === null" class="col-md-6 col-xs-12">
  <div class="row">
    <div class="col-md-offset-2 col-md-8 col-md-offset-2"><h3>Add partner types so that when you register a partner/client there will be a drop down filled with list of types to choose from.</h3></div>
  </div>
</div>

</div>
</template>
<script>
import PartnerService from "../../../../../common/api.service";
import router from '../../../../../router'
import store from '@/store'
import { CHECK_AUTH } from '@/store/actions.type'

export default {
  data() {
    return {
      partnerType: {
        Name: "",
        Description: ""
      }
    };
  },
  methods: {
    saveModel() {
      store.dispatch(CHECK_AUTH)
      console.log("Your data: " + JSON.stringify(this.partnerType));
      PartnerService.post("newpartnertype", this.partnerType);
      router.push({ name: 'Partner Types' })
    }
  }
};
</script>
<style>
</style>
