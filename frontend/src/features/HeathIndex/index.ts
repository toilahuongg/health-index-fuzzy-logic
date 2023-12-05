import { ResourceProps } from "react-admin";
import { LocalGroceryStore } from "@mui/icons-material";
import HeathIndexCreate from "./Create";
import HeathIndexShow from "./Detail";
import HeathIndexList from "./List";

const resourceHeathIndex: ResourceProps = {
  name: 'heath-index',
  icon: LocalGroceryStore,
  options: { label: 'Kiểm tra sức khoẻ' },
  list: HeathIndexList,
  create: HeathIndexCreate,
  show: HeathIndexShow,
  hasShow: true,
  hasCreate: true,
  hasEdit: false,

}
export default resourceHeathIndex;