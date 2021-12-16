using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web;
using System.Web.Http;
using TresureAPIService.Services;
using System.IO;
using System.Text;
using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Blob;
using TresureAPIService.Helper;

namespace TresureAPIService.Controllers
{
	public class UploadImageController : ApiController
	{
		// GET api/<controller>
		public IEnumerable<string> Get()
		{
			return new string[] { "value1", "value2" };
		}

		// GET api/<controller>/5
		public string Get(int id)
		{
			return "value";
		}

		[HttpPost]
		// POST api/<controller>
		public async Task<HttpResponseMessage> UploadImage()
		{
			ImageService imageService = new ImageService();
			HttpResponseMessage result = null;
			var httpRequest = HttpContext.Current.Request;
			if (httpRequest.Files.Count > 0)
			{
				var docfiles = new List<string>();
				foreach (string file in httpRequest.Files)
				{
					var postedFile = httpRequest.Files[file]; //get upload files contents, from esp32 camara photo.
					var imageUrl = await imageService.UploadImageAsync(postedFile);
					string imageName = imageService.Name;
					if (imageUrl != null)
					{
						Console.WriteLine(imageUrl.ToString());
						string url = "https://7e6b-125-227-38-129.ngrok.io/?photo=" + imageName; //url�Φ�:"ip/?photo="+�Ѽ�+ ���ڴ��J�Ѽ�
						string res = GetHttpResponse(url, 6000);
						if (res != null)
						{
							Console.WriteLine(res);
						}
					}
					else
					{
						result = Request.CreateResponse(HttpStatusCode.BadRequest);
					}
				}
				result = Request.CreateResponse(HttpStatusCode.Created, docfiles);
			}
			else
			{
				result = Request.CreateResponse(HttpStatusCode.BadRequest);
			}
			return await Task.FromResult(result);
		}
		public static string GetHttpResponse(string url, int Timeout)
		{
			HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
			request.Method = "GET";
			request.ContentType = "charset=UTF-8";
			request.UserAgent = null;
			//request.Timeout = Timeout;

			HttpWebResponse response = (HttpWebResponse)request.GetResponse();
			Stream myResponseStream = response.GetResponseStream();
			StreamReader myStreamReader = new StreamReader(myResponseStream, Encoding.GetEncoding("utf-8"));
			string retString = myStreamReader.ReadToEnd();
			myStreamReader.Close();
			myResponseStream.Close();

			return retString;
		}
	}
}
