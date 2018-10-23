$(function() {
		$("#search_result").hide();
		$("#sub_search").click(function() {
			$("#search_result").slideDown(1000);
		});

		var $demo_result = $('#demo_result');
		$demo_result.bootstrapTable({
			method : "get", //使用get请求到服务器获取数据
			url : "/demo/result",
			contentType : 'application/json,charset=utf-8',
			dataType : "json",
			responseHandler : function(e) {
				console.log(e);
				if (e.content && e.content.length > 0) {
					return {
						"rows" : e.content,
						"total" : e.totalElements
					};
				} else {
					return {
						"rows" : [],
						"total" : 0
					};
				}
			},
			queryParams : function(params) {
				return {
					pageNum : Math.ceil(params.offset / params.limit) + 1,
					pageSize : params.limit,
					order : params.order,
					ordername : params.sort
				//startDateTime : $("#dateSearch .startDate").val(),
				//endDateTime : $("#dateSearch .endDate").val(),
				//search : $("#dateSearch .imuserid").val()
				};
			},
			pagination : true,//显示分页条：页码，条数等 
			sortOrder:'ASC',//排序方式
			striped : true,//隔行变色 
			pageNumber : 1,//首页页码 
			pageSize : 10,//分页，页面数据条数 
			uniqueId : "id",//Indicate an unique identifier for each row 
			sidePagination : "server",//在服务器分页
			toolbar : "#toolbar",//工具栏
			search : false,//搜索
			searchOnEnterKey : false,
			showRefresh : false,//刷新
			showToggle : false,//
			columns : [
					{
						title : '序号',
						//field : 'name',
						align : 'center',
						formatter : function(value, row, index) {
							return index + 1;
						}
					},
					{
						title : '推荐股票',
						field : 'name',
						align : 'center',
						valign : 'middle',
					},
					{
						title : '股票代码',
						field : 'code',
						align : 'center'
					},
					{
						title : '操作',
						field : 'id',
						align : 'center',
						visible : false,
						formatter : function(value, row, index) {
							var e = '<a href="#" mce_href="#" onclick="edit(\''
									+ row.id + '\')">编辑</a> ';
							var d = '<a href="#" mce_href="#" onclick="del(\''
									+ row.id + '\')">删除</a> ';
							return e + d;
						}
					} ]
		});
		
		var $demo_data = $('#demo_data');
		$demo_data.bootstrapTable({
			method : "get", //使用get请求到服务器获取数据
			url : "/demo/data",
			contentType : 'application/json,charset=utf-8',
			dataType : "json",
			responseHandler : function(e) {
				console.log(e);
				if (e && e.length > 0) {
					return {
						"rows" : e,
						"total" : e.size
					};
				} else {
					return {
						"rows" : [],
						"total" : 0
					};
				}
			},
			queryParams : function(params) {
				return {
					pageNum : Math.ceil(params.offset / params.limit) + 1,
					pageSize : params.limit,
					order : params.order,
					ordername : params.sort
				};
			},
			pagination : false,//显示分页条：页码，条数等 
			striped : true,//隔行变色 
			pageNumber : 1,//首页页码 
			pageSize : 10,//分页，页面数据条数 
			uniqueId : "id",//Indicate an unique identifier for each row 
			sidePagination : "server",//在服务器分页
			toolbar : "#toolbar",//工具栏
			search : false,//搜索
			searchOnEnterKey : false,
			showRefresh : false,//刷新
			showToggle : false,//
			columns : [
					{title : ' ',	field : 'name',	align : 'center',valign : 'middle'},
					{title : 'TOP_1',	field : 'top1',	align : 'center'},
					{title : 'TOP_2',	field : 'top2',	align : 'center'},
					{title : 'TOP_3',	field : 'top3',	align : 'center'},
					{title : 'TOP_4',	field : 'top4',	align : 'center'},
					{title : 'TOP_5',	field : 'top5',	align : 'center'},
					{title : 'TOP_6',	field : 'top6',	align : 'center'},
					{title : 'TOP_7',	field : 'top7',	align : 'center'},
					{title : 'TOP_8',	field : 'top8',	align : 'center'},
					{title : 'TOP_9',	field : 'top9',	align : 'center'},
					{title : 'TOP_10',	field : 'top10',	align : 'center'},
					{title : 'TOP_11',	field : 'top11',	align : 'center'},
					{title : 'TOP_12',	field : 'top12',	align : 'center'}
			]
		});
		
	});