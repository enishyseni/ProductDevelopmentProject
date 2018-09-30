<template>
  <div class="card">
    <div class="header">
      <h4 class="title">Edit Profile</h4>
    </div>
    <div class="content">
      <form>
        <div class="row">
          <div class="col-md-5">
            <fg-input type="text"
                      label="Partner Type"
                      :disabled="true"
                      placeholder="Partner type id"
                      v-model="partner.PartnerType">
            </fg-input>
          </div>
          <div class="col-md-3">

            <fg-input type="text"
                      label="Name"
                      placeholder="Name"
                      v-model="partner.OrganisationName">
            </fg-input>
          </div>
          <div class="col-md-4">
            <fg-input type="email"
                      label="Username"
                      placeholder="Email"
                      v-model="partner.OrganisationDescription">
            </fg-input>
          </div>
        </div>
       
        <div class="text-center">
          <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="addPartner">
            Add Partner
          </button>
        </div>
        <div class="clearfix"></div>
      </form>
    </div>
  </div>
</template>
<script>
  import PartnerService from '../../../../../common/api.service'
  export default {    
    data () {
      return {
        partner: {
          company: 'Paper Dashboard',
          username: 'michael23',
          email: '',
          lastName: 'Faker',
          address: 'Melbourne, Australia',
          city: 'melbourne',
          postalCode: '',
          aboutMe: `Oh so, your weak rhyme. You doubt I'll bother, reading into it.I'll probably won't, left to my own devicesBut that's the difference in our opinions.`
        }
      }
    },
    methods: {
      addPartner () {
        alert('Your data: ' + JSON.stringify(this.partner))
      }
    }
  }

</script>
<style>

</style>
