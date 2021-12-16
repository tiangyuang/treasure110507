using System;
using System.Net;
using System.IO;
//using Microsoft.AspNetCore.Mvc.ViewFeatures;
//using NPOI.SS.Formula.Functions;
using System.Text;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string url = "http://d379-211-21-101-137.ngrok.io"; //url形式:"ip/?photo="+參數+".jpg" 幫我插入參數
            string res = GetHttpResponse(url, 6000);
            if (res != null)
            {
                Console.WriteLine(res);
            }
        }
        ///
        /// Get請求
        /// 
        /// 
        /// 字串
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
