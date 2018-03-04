var error_name = true;
var error_password = true;
var error_check_password = true;
var error_email = true;
var error_check = false;

$(function(){

	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#user_name').focus(function () {
		$('#user_name').next().hide();
    });

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#pwd').focus(function () {
		$('#pwd').next().hide();
    });

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#cpwd').focus(function () {
		$('#cpwd').next().hide();
    });

	$('#email').blur(function() {
		check_email();
	});

	$('#email').focus(function () {
		$('#email').next().hide();
    });

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});

	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}
		
	}




});

function check_user_name(){
	var user_name = $('#user_name').val();
	var tip = $('#user_name').next();
	var len = user_name.length;
	if(len<5||len>20)
	{
		tip.html('请输入5-20个字符的用户名');
		tip.show();
		error_name = true;
	}
	else
	{
		// 判断用户名是否存在
		$.get("/user/user_name_validate/",{name: user_name}, function(data){
			if("0"!=data){
				tip.html('该用户名已存在！');
				tip.show();
				error_name = true;
			} else {
				tip.hide();
				error_name = false;
			}
		});

	}
}

function check_pwd(){
	var len = $('#pwd').val().length;
	if(len<8||len>20)
	{
		$('#pwd').next().html('密码最少8位，最长20位');
		$('#pwd').next().show();
		error_password = true;
	}
	else
	{
		$('#pwd').next().hide();
		error_password = false;
	}
}

function check_email(){
	var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

	if(re.test($('#email').val()))
	{
		$('#email').next().hide();
		error_email = false;
	}
	else
	{
		$('#email').next().html('你输入的邮箱格式不正确');
		$('#email').next().show();
		error_check_password = true;
	}

}

function check_submit(){

    check_pwd();
    check_email();
    if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
    {
        return true;
    }
    else
    {
        return false;
    }
}