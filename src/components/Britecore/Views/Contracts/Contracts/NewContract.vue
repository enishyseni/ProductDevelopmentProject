<template>
    <div class="row">
      <div class="col-md-6 col-xs-12">
        <div class="col-md-12 col-xs-12">
            <div class="card">
                <div class="header">
                    <h4 class="title">Select partner and a member</h4>
                </div>
                <div class="content">
                    <form>

                        <div class="row">
<div class="col-md-12 col-xs-12">
                            <div class="form-group">
                                <label for="sel1">Partner (create if not in the list)</label>
                                <select class="form-control" id="sel1">
                                    <option>Partner 1</option>
                                    <option>Partner 2</option>
                                    <option>Partner 3</option>
                                    <option>Partner 4</option>
                                </select>
                            </div>
</div>
<div class="col-md-12 col-xs-12">
                            <div class="form-group">
                                <label for="sel1">Partner member (create if not in the list):</label>
                                <select class="form-control" id="sel1">
                                    <option>Partner member 1</option>
                                    <option>Partner member 2</option>
                                    <option>Partner member 3</option>
                                    <option>Partner member 4</option>
                                </select>
                            </div>
</div>
                        </div>

                        <div class="row">
                            <div class="text-center">
                                <button type="submit" class="btn btn-warning btn-fill btn-wd" @click.prevent="saveModel">
                                    Add new partner
                                </button>
                                <button type="submit" class="btn btn-warning btn-fill btn-wd" @click.prevent="saveModel">
                                    Add partner member
                                </button>
                            </div>
                        </div>

                        <div class="clearfix"></div>
                    </form>
                </div>

            </div>

        </div>

        <div class="col-md-12 col-xs-12">
            <div class="card">
                <div class="header">
                    <h4 class="title">Select contract definitions</h4>
                </div>
                <div class="content">
                    <form>

                        <div class="row">
<div class="col-md-12 col-xs-12">
                            <div class="table-full-width table-responsive">
                                <table class="table table-hover">
                                    <thead>
                                        <th>#</th>
                                        <th>Definition name</th>
                                        <th>Insurance policy</th>
                                        <th>Entity or Asset</th>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>
                                                1
                                            </td>
                                            <td>
                                                Def x
                                            </td>
                                            <td>
                                                Ins.Pol x
                                            </td>
                                            <td>
                                                Asset x
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                2
                                            </td>
                                            <td>
                                                Def y
                                            </td>
                                            <td>
                                                Ins.Pol y
                                            </td>
                                            <td>
                                                Asset y
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                3
                                            </td>
                                            <td>
                                                Def z
                                            </td>
                                            <td>
                                                Ins.Pol z
                                            </td>
                                            <td>
                                                Entity z
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
</div>
<div class="col-md-12 col-xs-12">
                            <div class="form-group">
                                <label for="sel1">Definition (create if not in the list)</label>
                                <select class="form-control" id="sel1">
                                    <option>Def x</option>
                                    <option>Def y</option>
                                    <option>Def z</option>
                                </select>
                            </div>
</div>
                        </div>

                        <div class="row">
                            <div class="text-center">
                                <button type="submit" class="btn btn-warning btn-fill btn-wd" @click.prevent="saveModel">
                                    Add selected definition
                                </button>
                                <button type="submit" class="btn btn-warning btn-fill btn-wd" @click.prevent="saveModel">
                                    Add new definition
                                </button>
                            </div>
                        </div>

                        <div class="clearfix"></div>
                    </form>
                </div>

            </div>

        </div>

        <div class="col-md-12 col-xs-12">
            <div class="card">
                <div class="header">
                    <h4 class="title">Add insurance compliance document requests (or upload if already available)</h4>
                </div>
                <div class="content">
                    <form>

                        <div class="row">
<div class="col-md-12 col-xs-12">
                            <div class="table-full-width table-responsive">
                                <table class="table table-hover">
                                    <thead>
                                        <th>#</th>
                                        <th>Document name</th>
                                        <th>(upload if available)</th>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>
                                                1
                                            </td>
                                            <td>
                                                Doc x
                                            </td>
                                            <td>
                                                <button type="button" class="btn btn-just-icon btn-outline-success"><!----><i class="fa fa-envelope"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                2
                                            </td>
                                            <td>
                                                Doc y
                                            </td>
                                            <td>
                                                <button type="button" class="btn btn-just-icon btn-outline-success"><!----><i class="fa fa-envelope"></i></button>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                3
                                            </td>
                                            <td>
                                                Doc z
                                            </td>
                                            <td>
                                                <button type="button" class="btn btn-just-icon btn-outline-success"><!----><i class="fa fa-envelope"></i></button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
</div>
<div class="col-md-12 col-xs-12">
                            <div class="form-group">
                                <label for="sel1">Definition (create if not in the list)</label>
                                <select class="form-control" id="sel1">
                                    <option>Doc x</option>
                                    <option>Doc y</option>
                                    <option>Doc z</option>
                                </select>
                            </div>
</div>

                        </div>

                        <div class="row">
                            <div class="text-center">
                                <button type="submit" class="btn btn-warning btn-fill btn-wd" @click.prevent="saveModel">
                                    Add selected document
                                </button>
                                <button type="submit" class="btn btn-warning btn-fill btn-wd" @click.prevent="saveModel">
                                    Add new document request
                                </button>
                            </div>
                        </div>

                        <div class="clearfix"></div>
                    </form>
                </div>

            </div>

        </div>


            <div class="col-md-12 col-xs-12">
                <div class="text-center">
                  <div class="row">
                    <div class="col-md-offset-1 col-md-3">
                    <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="saveModel">
                        Save as draft
                    </button>
                    </div>
                    <div class="col-md-4">
                    <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="saveModel">
                        Save as opportunity
                    </button>
                    </div>
                    <div class="col-md-3 col-md-offset-1">
                    <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="saveModel">
                        Initiate
                    </button>
                    </div>
                  </div>
                </div>
            </div>
    
</div>
<div class="col-md-6 col-xs-12">
        <div class="col-md-12 col-xs-12">
            <div class="row">
                <div class="col-md-offset-2 col-md-8 col-md-offset-2">
                    <h3>Steps to prepare the insurance contract:</h3></div>
                <div class="col-md-offset-2 col-md-8 col-md-offset-2">
                    <h3>1. Select partner and a member or create new. If Partner is individual then only one select option will appear, if family or organisational then multiple options will appear.</h3></div>
                <div class="col-md-offset-2 col-md-8 col-md-offset-2">
                    <h3>2. Add contract definitions or create new. Contract definition needs to have a contract policy and Entity/Asset that it applies attached to it.</h3></div>
                <div class="col-md-offset-2 col-md-8 col-md-offset-2">
                    <h3>3. Add contract documents or create new. Define contract documents that will be requested for partner to provide them or upload them now.</h3></div>
                <div class="col-md-offset-2 col-md-8 col-md-offset-2">
                    <h3>Contract can be saved as a draft, opportunity, or initiate.</h3></div>
            </div>
        </div>
      </div>
    
    </div>
</template>
<script>
import PartnerService from "../../../../../common/api.service";
import router from "../../../../../router";
import store from "@/store";
import { CHECK_AUTH } from "@/store/actions.type";

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
      store.dispatch(CHECK_AUTH);
      console.log("Your data: " + JSON.stringify(this.partnerType));
      PartnerService.post("newpartnertype", this.partnerType);
      router.push({ name: "Partner Types" });
    }
  }
};
</script>
<style>
</style>
