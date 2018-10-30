stock = {
		init:function(){
			$.ajax({
				url : "/demo/config",
				data : {names:["day_threshold","week_threshold"]},
				dataType: "json",
				async : false,
				success : function(data) {
					for(i in data){
						if(data[i].name == 'day_threshold'){
							$("#day_rate").val(data[i].value);
						}else if(data[i].name == 'week_threshold'){
							$("#week_rate").val(data[i].value);
						}
					}
				}
			});
		},
		saveConfig:function(){
			data = [{name:"day_threshold",value:$("#day_rate").val()},
				{name:"week_threshold",value:$("#week_rate").val()}];
			$.ajax({
				type: "POST",
				url : "/demo/saveConfig",
				data : JSON.stringify(data),
				dataType: "json",
				contentType:"application/json;charset=utf-8",
				success : function(data) {
					for(i in data){
						if(data[i].name == 'day_threshold'){
							$("#day_rate").val(data[i].value);
						}else if(data[i].name == 'week_threshold'){
							$("#week_rate").val(data[i].value);
						}
					}
				}
			});
		}
}
$(function() {
	stock.init();
	$("#sub_sumbit").click(function() {
		stock.saveConfig();
	});
	$("#sub_parse").click(function(){
		stocks = $("#stock_list").val().length > 0 ? $("#stock_list").val().split(","):null;
		data = {dayRate:$("#day_rate").val(),weekRate:$("#week_rate").val(),stocks:stocks};
		$.ajax({
			type: "POST",
			url : "/demo/parse",
			timeout : 60000,
			data : JSON.stringify(data),
			dataType: "json",
			contentType:"application/json;charset=utf-8",
			success : function(data) {
				demo_table.bootstrapTable('load',data);
//				for(i in data){
//					$('#demo_table').bootstrapTable('insertRow',{ index: 1,'row':data[i]});
//				}
			},
			error:function(err){
				console.log(JSON.stringify(err));
				if(err.responseJSON && err.responseJSON.message)
					alert(err.responseJSON.message);
			}
		});
	});
	
	$("#sub_history").click(function(){
		$.ajax({
			type: "get",
			url : "/demo/history",
			data : "",
			dataType: "json",
			contentType:"application/json;charset=utf-8",
			success : function(data) {
				demo_table.bootstrapTable('load',data);
			},
			error:function(err){
				console.log(JSON.stringify(err));
				if(err.responseJSON && err.responseJSON.message)
					alert(err.responseJSON.message);
			}
		});
	});
	$("#sub_today").click(function(){
		$.ajax({
			type: "get",
			url : "/demo/today",
			data : "",
			dataType: "json",
			contentType:"application/json;charset=utf-8",
			success : function(data) {
				demo_table.bootstrapTable('load',data);
			},
			error:function(err){
				console.log(JSON.stringify(err));
				if(err.responseJSON && err.responseJSON.message)
					alert(err.responseJSON.message);
			}
		});
	});

	var demo_table = $('#demo_table');
	demo_table.bootstrapTable({
//		// url: '/demo/parse', //请求后台的URL（*） 
//		// method: 'post', //请求方式（*） 
//		toolbar: '#toolbar', //工具按钮用哪个容器 
//		striped: true, //是否显示行间隔色 
//		cache: false, //是否使用缓存，默认为true，所以一般情况下需要设置一下这个属性（*） 
//		pagination: true, //是否显示分页（*） 
//		sortOrder: "asc", //排序方式 
//		queryParams: oTableInit.queryParams,//传递参数（*） 
//		sidePagination: "client", //分页方式：client客户端分页，server服务端分页（*） 
//		pageNumber: 1, //初始化加载第一页，默认第一页 
//		pageSize: 5, //每页的记录行数（*） 
//		pageList: [10, 25, 50, 100], //可供选择的每页的行数（*） 
//		search: true, //是否显示表格搜索，此搜索是客户端搜索，不会进服务端，所以，个人感觉意义不大 
//		showColumns: true, //是否显示所有的列 
//		showRefresh: true, //是否显示刷新按钮 
//		minimumCountColumns: 2, //最少允许的列数 // 
//		clickToSelect: true, //是否启用点击选中行 
//		height: 500, //表格高度 
//		uniqueId: "id", //每一行的唯一标识，一般为主键列
		columns : [
			{title : '代码',	field : 'code',	align : 'center'},
			{title : '日期',	field : 'date',	align : 'center'},
			{title : '日换手率',	field : 'daily',	align : 'center'},
			{title : '周日期',	field : 'weekDay',	align : 'center'},
			{title : '周换手率',	field : 'weekly',	align : 'center'}
		]
	});
});